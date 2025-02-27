import json
import pandas as pd


def process_and_transform_file(input_path, output_path):
    try:

        intermediate_data = []
        prompt, response = "", ""

        # 读取excel文件
        df = pd.read_excel(input_path, engine='openpyxl')
        # 遍历读取样本的每行数据
        for row in df.itertuples():
            if row[1] and row[2]:
                prompt, response = row[1].strip(), row[2].strip()
                intermediate_data.append({"prompt": prompt, "response": response})
        with open(output_path, "w", encoding='utf-8') as output_file:
            for entry in intermediate_data:
                transformed_data = {
                    "messages": [
                        {"role": "user", "content": entry["prompt"]},
                        {"role": "assistant", "content": entry["response"]}
                    ]
                }
                output_file.write(json.dumps(transformed_data, ensure_ascii=False) + '\n')
        print(f"转换完成，文件保存至：{output_path}")
    except Exception as e:
        print(f"处理文件时发生错误：{e}")


input_path = "./数据.xlsx"
output_path = "./train.jsonl"
process_and_transform_file(input_path, output_path)