import pandas as pd

# 读取 Excel 文件
data = pd.read_excel(r'D:\0文献整理\网络入侵检测\KDD99\标签转换.xlsx')
original_labels = data['label1']

# 转化字典
label_mapping = {
    'dos': ['back', 'land', 'neptune', 'pod', 'smurf', 'teardrop'],
    'u2r': ['buffer_overflow', 'loadmodule', 'perl', 'rootkit'],
    'r2l': ['ftp_write', 'guess_passwd', 'imap', 'multihop', 'phf', 'spy', 'warezclient', 'warezmaster'],
    'probe': ['ipsweep', 'nmap', 'portsweep', 'satan'],
    'normal': ['normal'],
}

# 转化函数
def convert_labels(original_labels, label_mapping):
    converted_labels = []

    for label in original_labels:
        for new_label, original_labels_list in label_mapping.items():
            if label in original_labels_list:
                converted_labels.append(new_label)
                break
        else:
            # 如果标签不在映射字典中，则转化为'unknown'
            converted_labels.append('unknown')

    return converted_labels

# 进行标签转化
converted_labels = convert_labels(original_labels, label_mapping)

# 创建DataFrame
df = pd.DataFrame({'Original_Label': original_labels, 'Converted_Label': converted_labels})

# 保存为CSV文件
df.to_csv('converted_dataset_train.csv', index=False)
