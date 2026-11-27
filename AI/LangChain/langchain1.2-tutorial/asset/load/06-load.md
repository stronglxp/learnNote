# 自然语言处理技术文档

本文档用于测试`UnstructuredMarkdownLoader`的中文处理能力。

## 第一章：简介

自然语言处理(NLP)是人工智能的重要分支，主要技术包括：

- 文本分类
- 命名实体识别
- 机器翻译
- 情感分析
- 问答系统

## 第二章：关键技术

### 2.1 预训练模型

1. **BERT**：双向Transformer编码器
2. **GPT**：自回归语言模型  
3. **T5**：文本到文本转换框架

### 2.2 代码示例

```python
from transformers import pipeline

# 创建文本分类管道
classifier = pipeline("text-classification", model="bert-base-chinese")

result = classifier("这家餐厅的服务很棒！")
print(result)