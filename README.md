# 📊 ppt-generator-biz · 商业风格 PPT 生成器

> 生成纯 HTML 演示文稿，白底红字专业风格，一键部署到全球可访问 URL。

## 效果演示

👉 **在线预览（示例 PPT）：** https://nfleaqmy1z8w.space.minimaxi.com

主题：《AI 的生产力变革》，6 大章节，17 页内容，完整覆盖商业 PPT 全部版式。

---

## 安装方式

```
请安装 ppt-generator-biz 技能，帮我做一个工作汇报 PPT。
技能地址：https://github.com/EEvinci/ppt-generator-biz
```

## 功能一览

| 功能 | 说明 |
|------|------|
| 📄 封面页 | 标题 + 副标题 + 红色分割线，极简风格 |
| 📋 目录页 | 三列网格布局，序号清晰 |
| 📑 内容页 | 5-6 个卡片纵向排列，每卡片 5-7 句含案例 |
| 🔚 结尾页 | 金句收尾，白底极简 |
| 📱 响应式 | 16:9 横屏，支持键盘/触摸翻页 |
| 🚀 一键部署 | deploy 命令生成 CDN 可访问 URL |

## 触发词

- 「做个 PPT」「生成演示文稿」
- 「帮我做一个汇报 PPT」
- 「商业报告 PPT」「工作汇报」
- 「做个 slide」

## 工作流

```
1. 告诉我主题、受众、目的
   ↓
2. 我规划章节结构（4-6章节）
   ↓
3. 生成 build.py 脚本
   ↓
4. python3 build.py
   ↓
5. deploy /workspace/ppts/dist
   ↓
6. 分享 CDN URL 给观众
```

## 内容规范

**每页结构：**
- 标签徽章（如 `01 · 概念定义`）
- 页面标题
- 5-6 个卡片纵向排列
- 每个卡片：标题（粗体居中）+ 正文（居中，5-7句）

**内容充实度：** 每张卡片需包含具体案例、真实数字、逻辑解释，拒绝空洞结论。

## 版式风格

- 配色：白底 `#fff` + 近黑 `#1a1a2e` + 红色强调 `#c0392b`
- 字体：PingFang SC / Microsoft YaHei
- 交互：键盘左右箭头 / 空格 / 触摸滑动翻页

## 技术栈

- 纯 HTML + CSS + JavaScript（零依赖）
- Python 3（用于生成 HTML）
- 无需安装任何 npm 包或 Python 库

## GitHub

- 仓库：github.com/EEvinci/ppt-generator-biz
- 许可证：MIT
