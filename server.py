import http.server
import json
import os
import urllib.parse

PORT = int(os.environ.get('PORT', 8080))
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def address_string(self):
        # Prevent slow DNS lookups when logging requests
        return self.client_address[0]

    def do_GET(self):
        # Decode and clean path to handle URL-encoded characters and query parameters
        path_clean = urllib.parse.unquote(self.path).split('?')[0]
        
        # Intercept quote HTML requests in Service_quote directory, excluding viewer.html
        if path_clean.startswith('/Service_quote/') and path_clean.endswith('.html'):
            filename = os.path.basename(path_clean)
            if filename != 'viewer.html':
                json_filename = filename.replace('.html', '.json')
                json_path = os.path.join(DIRECTORY, 'Service_quote', json_filename)
                
                # If the parameters file exists, serve the dynamic viewer instead
                if os.path.exists(json_path):
                    viewer_path = os.path.join(DIRECTORY, 'Service_quote', 'viewer.html')
                    if os.path.exists(viewer_path):
                        try:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html; charset=utf-8')
                            self.end_headers()
                            with open(viewer_path, 'r', encoding='utf-8') as f:
                                self.wfile.write(f.read().encode('utf-8'))
                            return
                        except Exception as e:
                            pass # Fallback to default SimpleHTTPRequestHandler

        if self.path == '/api/list-quotes':
            try:
                service_quote_dir = os.path.join(DIRECTORY, 'Service_quote')
                if not os.path.exists(service_quote_dir):
                    os.makedirs(service_quote_dir, exist_ok=True)
                
                files = []
                json_basenames = set()
                
                # First, find all JSON files
                for f in os.listdir(service_quote_dir):
                    file_path = os.path.join(service_quote_dir, f)
                    if not os.path.isfile(file_path):
                        continue
                    if f.endswith('.json') and f not in ['package.json', 'package-lock.json']:
                        json_basenames.add(f.replace('.json', ''))
                        stat = os.stat(file_path)
                        html_filename = f.replace('.json', '.html')
                        files.append({
                            "filename": html_filename,
                            "mtime": stat.st_mtime,
                            "size": stat.st_size,
                            "is_template": False
                        })
                
                # Next, find all HTML files (legacy HTML without JSON)
                for f in os.listdir(service_quote_dir):
                    file_path = os.path.join(service_quote_dir, f)
                    if not os.path.isfile(file_path):
                        continue
                    if f.endswith('.html') and f != 'viewer.html':
                        basename = f.replace('.html', '')
                        if basename not in json_basenames:
                            # Legacy HTML quote with no JSON counterpart
                            stat = os.stat(file_path)
                            files.append({
                                "filename": f,
                                "mtime": stat.st_mtime,
                                "size": stat.st_size,
                                "is_template": False
                            })
                
                # Sort by mtime descending (newest first)
                files.sort(key=lambda x: x['mtime'], reverse=True)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(files).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/api/share-quote':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                quote_data = data.get('data', {})
                filename = data.get('filename', 'bao-gia')
                
                # Sanitize filename
                safe_filename = "".join(c for c in filename if c.isalnum() or c in ('-', '_')).strip()
                if not safe_filename:
                    safe_filename = 'bao-gia'
                
                # Ensure Service_quote directory exists
                service_quote_dir = os.path.join(DIRECTORY, 'Service_quote')
                os.makedirs(service_quote_dir, exist_ok=True)
                
                file_path = os.path.join(service_quote_dir, f"{safe_filename}.json")
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(quote_data, f, ensure_ascii=False, indent=2)
                
                # Return the URL dynamically based on the request Host header
                host = self.headers.get('Host', f'localhost:{PORT}')
                proto = self.headers.get('X-Forwarded-Proto', 'http')
                share_url = f"{proto}://{host}/Service_quote/{safe_filename}.html"
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"url": share_url, "filename": f"{safe_filename}.html"}
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"error": str(e)}
                self.wfile.write(json.dumps(response).encode('utf-8'))
        elif self.path == '/api/delete-quote':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                filename = data.get('filename', '')
                
                print(f"=== DELETE QUOTE REQUEST ===", flush=True)
                print(f"Filename received: {filename}", flush=True)
                
                # Safety check against path traversal
                is_valid_ext = filename.endswith('.html') or filename.endswith('.json')
                if not filename or '/' in filename or '\\' in filename or filename == '..' or not is_valid_ext:
                    print(f"Error: Invalid filename or path traversal detected.", flush=True)
                    self.send_response(400)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "Tên file không hợp lệ"}).encode('utf-8'))
                    return
                
                # Protect viewer page
                check_filename = filename if filename.endswith('.html') else filename.replace('.json', '.html')
                if check_filename == 'viewer.html':
                    print(f"Error: System templates cannot be deleted: {filename}", flush=True)
                    self.send_response(403)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "Không thể xóa file mẫu hệ thống"}).encode('utf-8'))
                    return
                
                if filename.endswith('.html'):
                    json_filename = filename.replace('.html', '.json')
                    html_filename = filename
                else:
                    json_filename = filename
                    html_filename = filename.replace('.json', '.html')
                
                service_quote_dir = os.path.join(DIRECTORY, 'Service_quote')
                
                # Support deleting both .json and legacy .html files
                file_path = os.path.join(service_quote_dir, json_filename)
                html_path = os.path.join(service_quote_dir, html_filename)
                
                print(f"JSON Path: {file_path} (Exists: {os.path.exists(file_path)})", flush=True)
                print(f"HTML Path: {html_path} (Exists: {os.path.exists(html_path)})", flush=True)
                
                deleted_any = False
                if os.path.exists(file_path):
                    try:
                        os.remove(file_path)
                        print(f"Deleted JSON file: {file_path}", flush=True)
                        deleted_any = True
                    except Exception as ex:
                        print(f"Error deleting JSON file: {ex}", flush=True)
                        raise ex
                if os.path.exists(html_path):
                    try:
                        os.remove(html_path)
                        print(f"Deleted HTML file: {html_path}", flush=True)
                        deleted_any = True
                    except Exception as ex:
                        print(f"Error deleting HTML file: {ex}", flush=True)
                        raise ex
                
                if deleted_any:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": True}).encode('utf-8'))
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "Không tìm thấy file"}).encode('utf-8'))
            except Exception as e:
                import traceback
                traceback.print_exc()
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, CustomHTTPRequestHandler)
    print(f"=== EVG QUOTE GENERATOR SERVER RUNNING ===")
    print(f"Server is running on: http://localhost:{PORT}")
    print(f"Open in browser: http://localhost:{PORT}/price/builder.html")
    print(f"Press Ctrl+C to stop.")
    httpd.serve_forever()
