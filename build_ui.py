import os
import json
import re

def main():
    base_dir = "/Users/tinhluong/work_dir/research_prjs/ws_ai_adoptation"
    ref_doc_dir = os.path.join(base_dir, "presentation_doc")
    
    content = {}
    
    # Categories to look for
    categories = {
        "01_connected_platform": "ConnectED Platform",
        "02_agentic_stack": "Agentic AI Stack",
        "03_challenges_ops": "Challenges & AgentOps",
        "04_deployment_handouts": "Deployment Handouts"
    }
    
    for cat_dir, cat_name in categories.items():
        full_path = os.path.join(ref_doc_dir, cat_dir)
        if not os.path.exists(full_path):
            continue
            
        content[cat_dir] = {
            "title": cat_name,
            "files": {}
        }
        
        for file_name in os.listdir(full_path):
            if file_name.endswith(".md"):
                file_path = os.path.join(full_path, file_name)
                key = file_name[:-3] # remove .md
                with open(file_path, "r", encoding="utf-8") as f:
                    content[cat_dir]["files"][key] = f.read()
                    
    # Let's write the JSON content as a JS declaration
    js_content = f"const WORKSHOP_CONTENT = {json.dumps(content, ensure_ascii=False, indent=2)};"
    
    # Read the template.html
    template_path = os.path.join(base_dir, "template.html")
    if not os.path.exists(template_path):
        print("Error: template.html not found.")
        return
        
    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()
        
    # Replace placeholder
    output_html = html.replace("/* CONTENT_PLACEHOLDER */", js_content)
    
    output_path = os.path.join(base_dir, "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output_html)
        
    print(f"Successfully compiled index.html to {output_path}")

if __name__ == "__main__":
    main()
