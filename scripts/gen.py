#!/usr/bin/env python3
"""
ppt-generator-biz: 商业风格 16:9 HTML 演示文稿生成器
用法: python3 gen.py "<主题>" "<内容摘要>" <页数>
"""
import sys, os, json

TOPIC = sys.argv[1] if len(sys.argv) > 1 else "演示主题"
PAGES = int(sys.argv[2]) if len(sys.argv) > 2 else 12

# 默认内容
SLIDES = [
    {
        "type": "cover",
        "tag": "ld2",
        "tag_text": "封面",
        "title": TOPIC,
        "subtitle": "专业演示 · 2026",
        "bg": "g-w"
    },
    {
        "type": "overview",
        "tag": "lr",
        "tag_text": "Overview",
        "title": "内容概览",
        "items": ["Foundation · 基础层", "Interface · 接口层", "Agent · 智能体层", "Ecosystem · 生态层"],
        "bg": "g-w"
    },
    {
        "type": "section",
        "tag": "lr",
        "tag_text": "01 · Foundation",
        "title": "LLM 大语言模型",
        "points": [
            ("Encoder-Only · 仅编码器", "BERT 系列 · 文本分类 · 情感分析"),
            ("Encoder-Decoder · 编解码器", "T5 · BART · 翻译 · 摘要"),
            ("Decoder-Only · 仅解码器 ← 主流", "GPT · LLaMA · Claude · 代码生成")
        ],
        "accent": "cred",
        "bg": "g-w"
    },
    {
        "type": "section",
        "tag": "lr",
        "tag_text": "02 · 调优手段",
        "title": "Prompt Engineering",
        "points": [
            ("SYS · 系统提示词", "定义角色：身份、行为规则、约束边界"),
            ("USR · 用户提示词", "具体任务指令、Few-shot 示例、输出格式"),
            ("新趋势", "结构化输出 + Chain-of-Thought + Tree-of-Thought")
        ],
        "accent": "cred",
        "bg": "g-w"
    },
    {
        "type": "section",
        "tag": "lr",
        "tag_text": "03 · 训练",
        "title": "Fine-tuning & LoRA",
        "points": [
            ("Full Fine-tune", "全量参数更新 · 显存占用大 · 效果最好"),
            ("LoRA · 低秩适配", "只训练低秩矩阵 · 显存减少 70%+ · 2025 年主流"),
            ("2026 应用", "企业垂直领域微调 + RLHF 对齐")
        ],
        "accent": "cog",
        "bg": "g-y"
    },
    {
        "type": "section",
        "tag": "lr",
        "tag_text": "04 · 知识增强",
        "title": "RAG 检索增强生成",
        "points": [
            ("提升知识准确性", "外部知识库检索 + 生成结合"),
            ("实时更新", "无需重新训练模型"),
            ("2026 新趋势", "GraphRAG + Hybrid Search · 企业标配")
        ],
        "accent": "cbl",
        "bg": "g-w"
    },
    {
        "type": "section",
        "tag": "lr",
        "tag_text": "05 · Interface",
        "title": "Function Calling & MCP",
        "points": [
            ("Function Calling", "大模型调用外部工具执行具体操作"),
            ("MCP 协议", "Anthropic 主推 · 标准化协议 · 2025 年爆发"),
            ("A2A 协议", "跨厂商 Agent 互联互通标准")
        ],
        "accent": "cbl",
        "bg": "g-w"
    },
    {
        "type": "agent_loop",
        "tag": "lr",
        "tag_text": "06 · 核心",
        "title": "Agent 智能体",
        "bg": "g-d",
        "dark": True
    },
    {
        "type": "section",
        "tag": "lr",
        "tag_text": "07 · 协作",
        "title": "Multi-Agent 系统",
        "points": [
            ("Agent Teams（Anthropic）", "Claude Opus 4.6 内置 · 多角色分工 · 原生通信"),
            ("OpenAI Swarm", "Handoffs 交接机制 · 多 Agent 编排实验框架"),
            ("注意事项", "Token 消耗大 · 系统复杂度高 · 需谨慎使用")
        ],
        "accent": "cpurple",
        "bg": "g-w"
    },
    {
        "type": "section",
        "tag": "lr",
        "tag_text": "08 · 上下文",
        "title": "Context Engineering",
        "points": [
            ("高质量筛选", "信息密度 > 信息量"),
            ("有效压缩", "摘要 / 重要性排序 / 滑动窗口"),
            ("2026 趋势", "128K+ 上下文窗口普及，压缩能力成为核心竞争力")
        ],
        "accent": "cgrn",
        "bg": "g-w"
    },
    {
        "type": "section",
        "tag": "lr",
        "tag_text": "09 · 能力封装",
        "title": "Agent Skill 技能封装",
        "points": [
            ("本质", "将 Prompt + 工具 + 知识封装为可复用模块"),
            ("类比", "Agent Skill ≈ 子 Agent ≈ SOP 的沉淀和复用"),
            ("生态", "SkillHub · 2026 年收录 1.3 万+ Skills")
        ],
        "accent": "cog",
        "bg": "g-y"
    },
    {
        "type": "section",
        "tag": "lr",
        "tag_text": "10 · 框架",
        "title": "OpenClaw 开源框架",
        "points": [
            ("多平台接入", "飞书 · Telegram · Discord · 钉钉 · 企业微信"),
            ("Skill 生态", "SkillHub（1.3 万+ Skills，腾讯 CDN 加速）"),
            ("MCP + 记忆 + Cron", "支持 DeepSeek · 豆包 · GPT · Claude")
        ],
        "accent": "cbl",
        "bg": "g-w"
    },
    {
        "type": "section",
        "tag": "lr",
        "tag_text": "11 · 工程实践",
        "title": "Harness Engineering",
        "points": [
            ("约束机制", "Guardrails 护栏 · 权限边界 · 操作审计"),
            ("反馈回路", "自验证循环 · 纠错机制 · 持续改进"),
            ("数据佐证", "换 Harness 架构，AI 编程通过率 52.8% → 66.5%")
        ],
        "accent": "cred",
        "bg": "g-d",
        "dark": True
    },
    {
        "type": "connection",
        "tag": "lr",
        "tag_text": "Connection · 串联",
        "title": "12 技术点 · 如何串联",
        "bg": "g-w"
    },
    {
        "type": "end",
        "tag": "lr",
        "tag_text": "结尾",
        "title": "让 AI 从工具变成伙伴",
        "bg": "g-d",
        "dark": True
    }
]

def build_slide(s, i):
    bg = s.get("bg", "g-w")
    dark = s.get("dark", False)
    tag = s.get("tag", "ld2")
    tag_text = s.get("tag_text", "")
    title = s.get("title", "")
    accent = s.get("accent", "cred")

    container_class = "c-dark" if dark else ""
    extra_style = "color:#fff" if dark else ""

    if s["type"] == "cover":
        return f'''<!-- S{i+1} 封面 -->
<div class="s {bg} end {container_class}">
  <p style="font-size:.82em;color:{'#9ca3af' if not dark else '#6b7280'};letter-spacing:.12em;text-transform:uppercase;margin-bottom:1.2em;">{tag_text}</p>
  <h1 style="font-size:3.2em;color:{'#1a1a2e' if not dark else '#fff'};">{title}</h1>
  <p class="sub" style="color:{'#6b7280' if not dark else '#9ca3af'}">{s.get("subtitle","")}</p>
  <div class="bar" style="margin:.8em 0;background:{'#c0392b' if not dark else '#e74c3c'}"></div>
  <p class="txtx">← → 键盘翻页 &nbsp;·&nbsp; 触摸滑动</p>
</div>'''

    elif s["type"] == "overview":
        items_html = "".join([f'<div class="row"><span class="arrow">→</span><span class="rtxt">{it}</span></div>' for it in s.get("items",[])])
        return f'''<!-- S{i+1} {tag_text} -->
<div class="s {bg} left {container_class}">
  <span class="lbl {tag}">{tag_text}</span>
  <h2>{title}</h2>
  <div class="bar" style="background:{'#c0392b' if not dark else '#e74c3c'}"></div>
  <div class="feat">{items_html}</div>
</div>'''

    elif s["type"] == "section":
        bar_color = "#c0392b" if accent == "cred" else "#27ae60" if accent == "cgrn" else "#2980b9" if accent == "cbl" else "#d4a017"
        cls_color = {"cred": "cred", "cgrn": "cgrn", "cbl": "cbl", "cog": "cog", "cpurple": "cb-p"}.get(accent, "cred")
        def make_card(pt):
            c_color_map = {"cred": "cr", "cgrn": "cg", "cbl": "cb", "cog": "co"}
            c_cls = c_color_map.get(accent, "cr")
            return f'<div class="c c{c_cls}"><p class="ct">{pt[0]}</p><p class="cbdy">{pt[1]}</p></div>'
        points_html = "".join(make_card(p) for p in s.get("points", []))
        return f'''<!-- S{i+1} {tag_text} -->
<div class="s {bg} left {container_class}">
  <span class="lbl {tag}">{tag_text}</span>
  <h2>{title}</h2>
  <div class="bar" style="background:{bar_color}"></div>
  <div class="g3">{points_html}</div>
</div>'''

    elif s["type"] == "agent_loop":
        return f'''<!-- S{i+1} Agent Loop -->
<div class="s {bg} center {container_class}">
  <span class="lbl {tag}">{tag_text}</span>
  <h2 style="color:#fff">{title}</h2>
  <div class="trio">
    <div class="ic ic-r"><div class="ie">思考</div><p class="il il-r">LLM 推理规划</p></div>
    <span style="color:#6b7280;font-size:1.8em">→</span>
    <div class="ic ic-g"><div class="ie">行动</div><p class="il il-g">调用工具 / 执行</p></div>
    <span style="color:#6b7280;font-size:1.8em">→</span>
    <div class="ic ic-b"><div class="ie">观察</div><p class="il il-b">结果反馈 / 判断</p></div>
  </div>
  <p class="txts" style="color:#9ca3af;margin-top:2em">循环直到目标达成，或达到最大迭代次数</p>
</div>'''

    elif s["type"] == "connection":
        rows = [
            ("Foundation · 基础层", "LLM → Prompt → Fine-tune → RAG → Context", "cr"),
            ("Interface · 接口层", "Function Calling → MCP → A2A", "cb"),
            ("Agent · 智能体层", "Agent Loop → Multi-Agent → Context Eng.", "cg"),
            ("Ecosystem · 生态层", "Agent Skill → OpenClaw → Harness", "co"),
        ]
        def get_color(t):
            m = {"cr": "#c0392b", "cb": "#2980b9", "cg": "#27ae60", "co": "#d4a017"}
            return m.get(t, "#c0392b")
        conn_html = "".join(
            f'<div class="c" style="border-left:.35em solid {get_color(r[2])}"><p class="ct">{r[0]}</p><p class="cbdy">{r[1]}</p></div>'
            for r in rows
        )
        return f'''<!-- S{i+1} {tag_text} -->
<div class="s {bg} left {container_class}">
  <span class="lbl {tag}">{tag_text}</span>
  <h2>{title}</h2>
  <div class="bar" style="background:#c0392b"></div>
  <div class="g2">{conn_html}</div>
</div>'''

    elif s["type"] == "end":
        return f'''<!-- S{i+1} 结尾 -->
<div class="s {bg} end {container_class}">
  <div class="bar" style="width:3em;margin:0 auto 2em;background:{'#e74c3c' if dark else '#c0392b'}"></div>
  <h1 style="font-size:3em;text-align:center;color:{'#fff' if dark else '#1a1a2e'}">{title}</h1>
  <p class="sub" style="text-align:center;color:{'#9ca3af' if dark else '#6b7280'}">从 Foundation 到 Ecosystem · 从调优到 Harness</p>
  <div class="bar" style="width:3em;margin:.8em auto 0;background:{'#e74c3c' if dark else '#c0392b'}"></div>
  <p class="ft" style="color:{'#6b7280' if dark else '#d1d5db'}">Agent · Skill · OpenClaw · Harness Engineering</p>
</div>'''

    return ""

# Load template
tmpl = open(os.path.join(os.path.dirname(__file__), "template.html")).read()

# Build slides
slides_html = "\n".join(build_slide(s, i) for i, s in enumerate(SLIDES))

# Replace placeholder
html = tmpl.replace("{{TITLE}}", TOPIC)
html = html.replace("<!-- SLIDES_PLACEHOLDER -->", slides_html)
html = html.replace("1 / N", f"1 / {len(SLIDES)}")

# Save
out_dir = "/workspace/outputs/ppt-generator-biz"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "ppt.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"生成完成：{out_path}")
print(f"共 {len(SLIDES)} 页")
print(f"文件大小：{os.path.getsize(out_path)} bytes")
