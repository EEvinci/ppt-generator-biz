---
name: ppt-generator-biz
description: 商业风格 HTML 演示文稿生成器。生成 16:9 横屏专业 PPT，白底红字配色，适用于工作汇报/商业路演/技术分享。触发关键词：PPT、演示文稿、商业报告、工作汇报。
metadata: { "openclaw": { "emoji": "📊", "requires": { "bins": ["python3"], "env": [] } } }
---

# ppt-generator-biz

商业风格 16:9 HTML 演示文稿生成器。

## 设计规范（v14 迭代验证版）

### 分辨率
- **强制 16:9 横屏**：`max-width: 177.78vh; max-height: 56.25vw`
- 使用 `position: fixed` 全屏容器，`display: flex + align-items:center + justify-content:center` 居中
- **不要用 vw/vh 单位做字号**，浏览器默认字号最可靠

### 配色方案（已验证）
| 用途 | 颜色 |
|------|------|
| 背景 | #fff（纯白）|
| 标题主文字 | #1a1a2e（近黑）|
| 强调/红色系 | #c0392b |
| 绿色系 | #27ae60 |
| 蓝色系 | #2980b9 |
| 黄色系 | #c9970c |
| 紫色系 | #8e44ad |
| 次要文字 | #7f8c8d |
| 灰色文字 | #a0aec0 |

### 字号体系（已验证，字体够大不溢出）
| 元素 | 字号 |
|------|------|
| 页面标题 h1 | 3.2em |
| 章节标题 h2 | 2.6em |
| 副标题/sub | 1.2em |
| 正文 txt | 1.3em |
| 正文辅助 txts | 1.15em |
| 注释 txtx | 1.1em |
| 卡片标题 ct | 1.15em |
| 卡片正文 cbdy | 1.2em |
| 箭头 arrow | 1.2em |
| 流程标签 fi | 1.2em |
| 标签 lbl | 1.1em |
| 结尾页 h1 | 3.6em |

### 布局规则
- **所有内容居中**：`text-align:center` 写在全局 `.txt/.cbdy` 等类
- **三列卡片页**：一律改用 `flex-direction:column` 上下堆叠（不要 3 列横排，字会看不清）
- **两列卡片页**：`.g2` 保持左右排布
- **卡片 padding**：`.9em 1.2em` 以上，不要太紧
- **板块间距**：gap `.6em ~ .75em`，不要太小

### 背景规则
- **全白背景**：所有页面统一 `background:#fff`，不使用深色/灰色背景
- 彩色分区用**卡片左边框色条**区分（`.cr/.cg/.cb/.co/.cp`）
- **对比度原则**：浅色背景 + 深色文字，深色背景 + 浅色文字

### Emoji 使用
- 每页最多 1 个，或用 Unicode 符号替代
- 避免机械感 emoji，用纯文字和符号（✓ → 等）

### 翻页交互
- 键盘左右箭头 + 空格键翻页
- 触摸左右滑动
- 底部圆点可点击跳转
- 当前页码显示 `x / 17`

## 使用方法

### 直接编辑 HTML
修改 `/workspace/ppts/dist/index.html`，然后：
```bash
# 备份到 skill 模板
cp /workspace/ppts/dist/index.html /workspace/skills/ppt-generator-biz/scripts/template.html
cp /workspace/ppts/dist/index.html /workspace/outputs/ppt-generator-biz/ppt.html

# 部署
deploy /workspace/ppts/dist
```

### 通过 gen.py 生成
编辑 `scripts/gen.py` 中的 `SLIDES` 列表，然后运行生成。

## 内容结构（共 17 页）
1. 封面
2. AI 应用技术全景 Overview
3. LLM 竞争格局 2026
4. Transformer 三种架构
5. Prompt Engineering
6. Fine-tuning & LoRA
7. RAG 检索增强生成
8. Function Calling · MCP · A2A
9. Agent 智能体
10. Agent Loop
11. Multi-Agent 多智能体系统
12. Context Engineering
13. Agent Skill 技能封装
14. OpenClaw 开源 Agent 框架
15. Harness Engineering
16. 12 技术点串联
17. 结尾

## 经验总结（2026-04-07 迭代记录）

### 为什么改了 14 个版本
1. **竖屏 vs 横屏**：用户明确要求 16:9，必须在 HTML 容器层强制约束
2. **字体太小**：初始版本 .78em 太小的，连续加大到 1.3~3.6em 才够用
3. **三列排版**：Transformer/MCP/Harness 的 3 列横排字体被压缩看不清 → 全部改为上下堆叠
4. **居中**：标题和内容都要 `text-align:center`，不能只管标题
5. **背景统一**：深色/米白色背景让用户觉得不统一 → 全部改为纯白
6. **留白控制**：padding 太大浪费空间太小挤，用 3% 7% 比较均衡

### 核心心法
> **先求不破，再求好看** — 先保证内容完整显示，再追求美观
> **字号宁大勿小** — 用户说看不清，往往是大方向问题，不是细节
> **三列改上下** — 这是最重要的布局经验，3 列横排在小屏幕上必死
> **全白背景最安全** — 彩色背景搭配文字容易出对比度问题，白底最稳

### 文件位置
- 当前版本：`/workspace/ppts/dist/index.html`
- Skill 模板：`/workspace/skills/ppt-generator-biz/scripts/template.html`
- 历史备份：`/workspace/outputs/ppt-generator-biz/ppt.html`
- 最新部署：https://1pochtyal0zd.space.minimaxi.com
