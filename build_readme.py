import re
import os

DOC_FILES = [
    "docs/index.md",
    "docs/install.md",
    "docs/examples_cm1.md",
    "docs/examples_cm2.md",
    "docs/examples_log.md"
]

OUTPUT_FILE = "README.md"

def clean_mkdocs_syntax(text, is_main_file=False):
    # 1. 移除 Material 圖示
    text = re.sub(r':[a-zA-Z0-9_\-]+:', '', text)
    
    # 2. 轉換提示區塊 (!!! info) 為標準引用區塊
    text = re.sub(r'^!!!\s+\w+(?:\s+"([^"]+)")?\s*\n', r'> **\1**\n', text, flags=re.MULTILINE)
    text = re.sub(r'^\?\?\?\s+\w+(?:\s+"([^"]+)")?\s*\n', r'> **\1 (展開看更多)**\n', text, flags=re.MULTILINE)
    
    # 3. 處理標籤頁 (=== "Python")
    # 將其轉為清單項目或粗體，避免跟正常標題混淆
    text = re.sub(r'^===\s+"([^"]+)"\s*\n', r'**【 \1 】**\n', text, flags=re.MULTILINE)
    
    # 【關鍵修正】4. 自動降級標題
    # 如果不是第一個檔案，就將所有的 # 替換為 ## (也就是所有標題降一級)
    if not is_main_file:
        text = re.sub(r'^(#+)\s', r'#\1 ', text, flags=re.MULTILINE)
        
    return text

def main():
    combined_text = ""
    
    for i, file_path in enumerate(DOC_FILES):
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8-sig") as f:
                content = f.read()
                
                # 判斷是否為串接的第一個檔案
                is_main = (i == 0) 
                
                # 清理語法並調整標題
                cleaned_content = clean_mkdocs_syntax(content, is_main_file=is_main)
                
                # 加入到總字串中
                combined_text += cleaned_content + "\n\n---\n\n"
        else:
            print(f"警告: 找不到檔案 {file_path}")

    # 寫入根目錄的 README.md
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(combined_text)
        
    print(f"成功: 已自動生成乾淨版本的 {OUTPUT_FILE} 供 PyPI 使用！")

if __name__ == "__main__":
    main()