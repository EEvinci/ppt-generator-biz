#!/usr/bin/env python3
"""
ppt-generator-biz 生成脚本
布局：纵向卡片列表（简洁专业）
"""
import os, html as htmlmod

# ===== 修改这里 =====
TITLE = "演示标题"
SLIDES = [
    {"type":"cover","title":"演示标题","subtitle":"副标题 \xb7 2026"},
    {"type":"overview","title":"内容概览","items":[
        "章节一 \u2014 概念定义",
        "章节二 \u2014 核心原理",
        "章节三 \u2014 核心能力详解",
        "章节四 \u2014 应用场景",
        "章节五 \u2014 数据佐证",
        "章节六 \u2014 局限与行动",
    ]},
    # ===== 章节一：概念定义（2页）=====
    {"type":"section","tag":"01 \xb7 概念定义","title":"什么是 XX（基础定义与背景）","points":[
        ("基本定义","正文 5-7 句话。XX 是指……它在 YY 场景下发挥……作用，是理解整个主题的基础。比如……（具体案例或数据）。"),
        ("发展背景","正文 5-7 句话，历史沿革和演进脉络。XX 起源于 A 年……经历了 B、C 阶段，发展到今天的状态。背后驱动的核心因素是……"),
        ("为什么重要","正文 5-7 句话，为什么在当前时间节点变得关键。XX 的重要性体现在……驱动的核心因素是……这对 YY 群体意味着……"),
        ("误区澄清","正文 5-7 句话。常见误解：很多人以为 XX 是……实际上……正确的理解应该是……这里最容易踩的坑是……"),
        ("核心特征","正文 5-7 句话，XX 的三大核心特征是 A、B、C，各自在其中扮演什么角色，典型表现是什么。"),
    ]},
    {"type":"section","tag":"01 \xb7 概念定义","title":"概念延伸：深层结构与边界","points":[
        ("深层结构","正文 5-7 句话。XX 的深层结构由 A、B、C 三层构成，彼此之间的关系是……这解释了为什么 XX 会产生 YY 效果。"),
        ("与相关概念的差异","正文 5-7 句话。XX 容易和 A、B 这两个相关概念混淆，它们之间的核心区别是……在 YY 场景下，正确区分这一点非常重要。"),
        ("有效边界","正文 5-7 句话。XX 有效的前提条件是……在什么情况下会失效或不适用，比如当出现 A 情况时，XX 的效果会大打折扣。"),
        ("生命周期","正文 5-7 句话。XX 从兴起到成熟，经历了哪几个阶段，目前处于哪个阶段，这个阶段的核心特征是什么。"),
        ("常见陷阱","正文 5-7 句话。新手最容易犯的 A、B、C 三个错误，每一个背后都有真实案例——比如某公司因 XX 失败的原因是……"),
    ]},
    # ===== 章节二：核心原理（2页）=====
    {"type":"section","tag":"02 \xb7 核心原理","title":"底层逻辑：运作机制与关键变量","points":[
        ("核心运作机制","正文 5-7 句话。XX 的运作依赖于 A、B、C 三要素，核心机制是……具体通过……方式实现……这是理解整个系统运作的关键。"),
        ("关键变量一","正文 5-7 句话。第一个关键变量是 A，它决定了……当 A 变化时，XX 效果会出现……的差异。控制好 A 是达成预期效果的前提。"),
        ("关键变量二","正文 5-7 句话。第二个关键变量是 B，它对 XX 的影响体现在……B 的正常范围是……超出范围会触发……后果。"),
        ("关键变量三","正文 5-7 句话。第三个关键变量是 C，它的作用是……C 与 A、B 之间存在……关系，三者共同决定了 XX 的最终效果。"),
        ("变量交互效应","正文 5-7 句话。A、B、C 三个变量并非独立运作，它们之间存在……的交互效应。比如当 A 高而 B 低时，C 的效果会……"),
    ]},
    {"type":"section","tag":"02 \xb7 核心原理","title":"原理实战：与其他方案对比与边界条件","points":[
        ("与传统方案的差异","正文 5-7 句话。XX 对比传统方案（A、B），核心差异在于……优势是……这种差异在 YY 场景下尤为明显，效率提升可达……"),
        ("典型案例解析","正文 5-7 句话。一个完整案例：某公司/团队使用 XX 方法/原理，达到了 YY 效果（具体数字），核心成功要素是抓住了 A 要点。"),
        ("技术原理进阶","正文 5-7 句话。从技术角度深入理解：XX 的底层依赖于……原理，这决定了它的上限是……而实际使用中往往只发挥了……"),
        ("边界条件","正文 5-7 句话。XX 有效的前提条件是……在以下情况下可能失效：A 场景（后果是……）、B 场景（后果是……），使用时需特别注意。"),
        ("失败模式分析","正文 5-7 句话。XX 最典型的三种失败模式：①……原因在于……②……③……每一个都有真实案例支撑，避坑的核心是……"),
    ]},
    # ===== 章节三：核心能力（2页）=====
    {"type":"section","tag":"03 \xb7 核心能力","title":"核心能力一：定义、表现与方法","points":[
        ("能力定义","正文 5-7 句话。XX 能力具体指……它解决的核心问题是……与普通做法的本质区别在于……具备这个能力是达到 A 水准的基本门槛。"),
        ("能力表现","正文 5-7 句话。具备 XX 能力后，可以做到……对比没有这个能力的情况：做 A 事原本需要 YY 时间，有了 XX 后只需 ZZ，效率提升……倍。"),
        ("实操方法：第一步","正文 5-7 句话。实现 XX 能力的第一步是……具体操作是……关键点在于……常见错误是……正确做法是……"),
        ("实操方法：第二步","正文 5-7 句话。第二步的核心是……实施路径是……需要的工具/资源是……这里最容易在 A 环节出问题，建议……"),
        ("实操方法：第三步","正文 5-7 句话。第三步是……这是将前两步整合起来形成闭环的关键一步。完成后，你应该能看到……效果，这标志着 XX 能力初步形成。"),
    ]},
    {"type":"section","tag":"03 \xb7 核心能力","title":"核心能力二：实战案例与常见错误","points":[
        ("能力定义","正文 5-7 句话。第二个核心能力（YY 能力）具体指……它与 XX 能力的互补关系是……两者结合使用时的效果是……"),
        ("能力表现与量化","正文 5-7 句话。YY 能力的具体表现：可以做到……效果量化：原本……现在……提升幅度……与同类方案相比，YY 的独特价值在于……"),
        ("真实案例：成功","正文 5-7 句话。案例：XX 公司/个人通过掌握 YY 能力，在 ZZ 场景下取得了……效果（具体数字）。成功的关键因素是……值得学习的做法是……"),
        ("真实案例：失败","正文 5-7 句话。对比案例：某团队试图应用 YY 能力，但因……（具体错误）导致……（失败后果）。这个案例的教训是……"),
        ("常见错误汇总","正文 5-7 句话。YY 能力最常见的 A、B、C 三个错误。错误一：很多人以为……实际上……正确做法是……"),
    ]},
    # ===== 章节四：应用场景（2页）=====
    {"type":"section","tag":"04 \xb7 应用场景","title":"典型场景一：背景、方案与效果","points":[
        ("场景背景","正文 5-7 句话。这个场景的具体背景：在什么情况下会用到 XX，典型用户是……他们在没有 XX 之前面临的核心挑战是……每年因此付出的成本是……"),
        ("解决方案","正文 5-7 句话。XX 如何解决这个场景的问题。具体做法：第一步……第二步……第三步……关键节点是……需要哪些资源配合……"),
        ("效果量化","正文 5-7 句话。实施后的效果数据：A 指标提升了 B%（具体来源），B 指标变化是……C 问题减少了 D%……整体效率提升 E 倍……这是来自 F 机构/企业的真实数据。"),
        ("成本与 ROI","正文 5-7 句话。实施 XX 的成本：初期投入……持续投入……ROI 测算：按当前效果，回收期约……如果规模扩大 N 倍，ROI 将提升至……"),
        ("用户证言","正文 5-7 句话。真实用户的声音：某企业 XX 说：「……」这代表了这个场景下用户的典型感受，核心共鸣点是……"),
    ]},
    {"type":"section","tag":"04 \xb7 应用场景","title":"典型场景二：选择建议与实施指南","points":[
        ("场景二背景","正文 5-7 句话。第二个典型场景：与场景一的差异在于……适用条件是……典型用户是……他们当前面临的痛点比场景一更……"),
        ("方案与效果","正文 5-7 句话。XX 在这个场景下的具体应用方案，实施路径和效果量化。效果数据：……（来自真实企业或机构），与场景一的效果差异在于……"),
        ("场景选择建议","正文 5-7 句话。什么情况下优先选场景一，什么情况下选场景二。判断标准：①……②……③……给观众的具体建议是……"),
        ("实施避坑指南","正文 5-7 句话。这个场景下实施 XX 最容易踩的 A、B、C 三个坑。每一个都有真实案例支撑，比如……最值得注意的避坑建议是……"),
        ("快速启动清单","正文 5-7 句话。如果观众今天就想尝试，需要准备的 A、B、C 三件事：第一步……（具体可操作），第二天……一周内可以看到的初期效果是……"),
    ]},
    # ===== 章节五：数据佐证（2页）=====
    {"type":"section","tag":"05 \xb7 数据佐证","title":"权威数据：机构报告与企业案例","points":[
        ("权威数据一","正文 5-7 句话。数据来源：XX 机构（名称）在 YY 年发布的报告，样本量是……数据显示……（具体数字）。这个数据的解读是……"),
        ("权威数据二","正文 5-7 句话。数据来源：XX 行业报告/学术论文，数据显示……（具体数字）。这个数据说明的趋势是……对从业者的启示是……"),
        ("权威数据三","正文 5-7 句话。数据来源：XX 企业官方披露/案例研究，具体数字是……该企业实施 XX 后，A 指标从……提升到……，B 指标改善了……"),
        ("市场整体数据","正文 5-7 句话。市场的整体采用率/规模数据：XX 机构数据显示……（年份、增长率、市场规模）。这说明……的趋势正在加速/放缓。"),
        ("数据综合结论","正文 5-7 句话。从以上数据看，核心结论是……这意味着……对观众的启发是：现在是介入的时机，因为……"),
    ]},
    {"type":"section","tag":"05 \xb7 数据佐证","title":"趋势预判：未来方向与对比洞察","points":[
        ("增长趋势","正文 5-7 句话。未来 1-3 年的核心趋势：XX 数据机构预测，到 YY 年……（规模/增长率），驱动这一增长的核心因素是……"),
        ("竞争格局变化","正文 5-7 句话。竞争格局的演变：目前 A、B、C 是头部玩家，格局正在向……方向变化。未来 1-2 年可能出现的变化是……"),
        ("使用前后对比","正文 5-7 句话。使用 XX 前后的典型对比数据：A 企业使用前……使用后……（具体指标），B 企业对比数据……综合提升幅度……"),
        ("ROI 测算参考","正文 5-7 句话。针对典型场景的 ROI 测算：以 A 企业为例，初期投入……月度持续成本……年度收益……ROI 约……回收期……"),
        ("趋势：长期价值","正文 5-7 句话。从 3-5 年视角看，XX 的长期价值体现在……早期布局者的先发优势正在积累，预计未来……"),
    ]},
    # ===== 章节五后插页：最佳实践（1页）=====
    {"type":"section","tag":"05 \xb7 最佳实践","title":"让效果最大化的六条最佳实践","points":[
        ("实践一：从小闭环开始","正文 5-7 句话。具体做法：不要一开始就追求大而全，而是从……切入，快速跑通一个最小闭环。比如……这样做的核心好处是……"),
        ("实践二：数据驱动迭代","正文 5-7 句话。建立数据指标体系，持续追踪……（A、B、C 指标）。通过数据发现问题的周期是……数据驱动决策的落地步骤是……"),
        ("实践三：跨部门协同","正文 5-7 句话。XX 落地需要 A、B、C 三个部门的配合，最容易在……环节出现分歧。解决方案是……成功案例：某企业通过……机制实现了跨部门高效协同。"),
        ("实践四：持续学习","正文 5-7 句话。团队如何保持对 XX 的持续学习和更新：建立……机制（A、B、C）。建议的节奏是……效果评估方式是……"),
        ("实践五：安全与合规先行","正文 5-7 句话。在启动 XX 之前，必须先确认……（A 合规要求、B 安全措施）。踩坑案例：某企业因忽视……导致……教训是……"),
        ("实践六：长期主义","正文 5-7 句话。XX 不是一次性项目，而是需要……的长期投入。短期、中期、长期各阶段的侧重点分别是……坚持长期投入的核心收益是……"),
    ]},
    # ===== 章节六：局限与行动（2页）=====
    {"type":"section","tag":"06 \xb7 局限与行动","title":"客观分析：局限、挑战与风险","points":[
        ("主要局限性","正文 5-7 句话。XX 的第一个主要局限性：边界在哪里……在 A 条件下效果会……比如 XX 机构的数据显示，当……时，准确率下降至……"),
        ("次要局限性","正文 5-7 句话。当前的技术瓶颈是……完全突破需要……在此之前，使用时需要有合理预期……"),
        ("主要挑战","正文 5-7 句话。当前行业面临的主要挑战：A 挑战（描述 + 原因 + 目前解法）、B 挑战……这些挑战的共同根源是……"),
        ("潜在风险","正文 5-7 句话。XX 的潜在风险：① A 风险（后果 + 发生概率）、② B 风险……最需要关注的是……风险控制的核心措施是……"),
        ("合规与伦理","正文 5-7 句话。特别注意事项：在 YY 场景下，XX 可能涉及……合规要求是……不注意可能导致……（真实案例），正确的做法是……"),
    ]},
    {"type":"section","tag":"06 \xb7 行动建议","title":"行动建议：从起点到长期深耕","points":[
        ("最小可行起点","正文 5-7 句话。第一步做什么：从 A 这个具体场景切入，建议投入……时间/资源，先跑通一个最小闭环……成功的标志是……"),
        ("分阶段路径","正文 5-7 句话。阶段一（A 周/月，B 目标）→ 阶段二（A 周/月，B 目标）→ 阶段三（A 周/月，B 目标）。每个阶段的关键里程碑是……"),
        ("工具与资源推荐","正文 5-7 句话。学习资源：A 书籍（适合入门）、B 书籍（进阶）、C 课程；工具推荐：A（免费/低成本，适合个人）、B（企业级，功能完整）"),
        ("核心注意事项","正文 5-7 句话。启动前需要确认的 A、B、C 三件事。比如：数据准备好了吗？Stakeholder 对齐了吗？内部能力匹配吗？避坑的核心是……"),
        ("长期深耕建议","正文 5-7 句话。如何在 XX 这个方向上持续深耕：① 短期（3个月内）关注……② 中期（6-12个月）达到……③ 长期（1-2年）成为……阶段的标志是什么。"),
    ]},
    # ===== 总结页 ======
    {"type":"section","tag":"07 \xb7 总结","title":"核心要点回顾与行动号召","points":[
        ("今天的关键收获","正文 5-7 句话。回顾今天的核心收获：①……②……③……这三个要点中，最核心的一个是……观众离开时最应该记住的是……"),
        ("立即可以开始的一件事","正文 5-7 句话。不要等到明天，今天就可以做的一件事是……（具体、可操作的第一步）。执行方式：……完成后会看到的效果是……"),
        ("常见误区提醒","正文 5-7 句话。最后提醒三个最常见的误区：①……（为什么很多人失败在这里）②……③……绕过它们的办法是……"),
        ("资源礼包","正文 5-7 句话。推荐给观众的最值得拥有的资源：A（书籍/课程/工具名称），核心价值是……适合人群是……获取方式：……"),
        ("金句收尾","正文 5-7 句话。一句话总结整个分享的核心观点，也是最想让观众记住的那句话。……（有力、有共鸣、有记忆点的金句）。"),
    ]},
    {"type":"end","title":"谢谢","subtitle":"让 XX 成为你真正的杠杆"},
]
# ===================

# ===== 以下勿动 =====
nums = ["01","02","03","04","05","06","07","08","09","10"]

CSS = (
    "*{margin:0;padding:0;box-sizing:border-box}"
    "html,body{width:100%;height:100%;overflow:hidden;background:#e8ecf0}"
    "body{font-family:'PingFang SC','Microsoft YaHei',Helvetica,sans-serif}"
    ".wrap{position:fixed;inset:0;display:flex;align-items:center;justify-content:center}"
    ".box{position:relative;width:100%;height:100%;max-width:177.78vh;max-height:56.25vw;background:#fff;overflow:hidden}"
    ".s{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding:4% 8%;opacity:0;transform:translateX(100%);transition:opacity .35s,transform .35s;pointer-events:none;background:#fff}"
    ".s.active{opacity:1;transform:translateX(0);pointer-events:auto}"
    ".s.prev{opacity:0;transform:translateX(-100%)}"
    ".cover-title{font-size:3.2em;font-weight:900;color:#1a1a2e;text-align:center;line-height:1.1;margin-bottom:.2em}"
    ".cover-bar{width:2.5em;height:3px;background:#c0392b;border-radius:2px;margin:.4em auto}"
    ".cover-sub{font-size:1.2em;color:#888;font-weight:300;text-align:center}"
    ".sec-header{display:flex;flex-direction:column;align-items:center;margin-bottom:.8em;width:100%}"
    ".tag-badge{display:inline-block;padding:.15em .9em;border-radius:999px;font-size:.75em;font-weight:700;letter-spacing:.06em;text-transform:uppercase;background:#fde8e8;color:#c0392b;border:1px solid #f5b7b1;margin-bottom:.5em}"
    ".page-title{font-size:2em;font-weight:900;color:#1a1a2e;text-align:center;line-height:1.15;margin-bottom:.15em}"
    ".bar-line{width:2.5em;height:3px;background:#c0392b;border-radius:2px;margin:0 auto 1em}"
    ".ov-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:.6em 1em;width:100%;max-width:960px}"
    ".ov-item{display:flex;flex-direction:row;align-items:flex-start;gap:.5em;padding:.5em .7em;background:#fafafa;border:1px solid #eaecf0;border-radius:.6em}"
    ".ov-num{font-size:.85em;font-weight:900;color:#c0392b;flex-shrink:0;min-width:1.6em}"
    ".ov-text{font-size:.95em;color:#333;line-height:1.5}"
    ".card-list{display:flex;flex-direction:column;gap:.5em;width:100%;max-width:960px}"
    ".card{background:#fff;border:1px solid #eaecf0;border-radius:.7em;padding:.6em 1em;box-shadow:0 1px 3px rgba(0,0,0,.05)}"
    ".card-title{font-size:1.05em;font-weight:700;color:#1a1a2e;margin-bottom:.15em;text-align:center}"
    ".card-body{font-size:.95em;color:#555;line-height:1.7;text-align:center}"
    ".end-bar{width:3em;height:3px;background:#c0392b;border-radius:2px;margin:0 auto}"
    ".end-title{font-size:3em;font-weight:900;color:#1a1a2e;text-align:center;line-height:1.2}"
    ".end-sub{font-size:1.2em;color:#888;margin-top:.8em;text-align:center}"
    ".dots{position:fixed;bottom:1em;left:50%;transform:translateX(-50%);display:flex;gap:.38em;z-index:300}"
    ".dot{width:.5em;height:.5em;border-radius:50%;background:rgba(0,0,0,.18);cursor:pointer;transition:all .25s}"
    ".dot.active{background:#c0392b;transform:scale(1.5)}"
    ".pg{position:fixed;bottom:1.9em;left:50%;transform:translateX(-50%);font-size:.75em;color:#bbb;z-index:300}"
)

parts = []
for i, s in enumerate(SLIDES):
    t = s["type"]
    if t == "cover":
        parts.append('<div class="s active" id="s%d"><h1 class="cover-title">%s</h1><div class="cover-bar"></div><p class="cover-sub">%s</p></div>' % (i, htmlmod.escape(s["title"]), htmlmod.escape(s["subtitle"])))
    elif t == "overview":
        cols = "".join('<div class="ov-item"><div class="ov-num">%s</div><div class="ov-text">%s</div></div>' % (nums[j], htmlmod.escape(s["items"][j])) for j in range(len(s["items"])))
        parts.append('<div class="s" id="s%d"><h2 class="page-title">%s</h2><div class="bar-line"></div><div class="ov-grid">%s</div></div>' % (i, htmlmod.escape(s["title"]), cols))
    elif t == "section":
        cards = "".join('<div class="card"><div class="card-title">%s</div><div class="card-body">%s</div></div>' % (htmlmod.escape(p[0]), htmlmod.escape(p[1])) for p in s["points"])
        parts.append('<div class="s" id="s%d"><div class="sec-header"><div class="tag-badge">%s</div><h2 class="page-title">%s</h2><div class="bar-line"></div></div><div class="card-list">%s</div></div>' % (i, htmlmod.escape(s["tag"]), htmlmod.escape(s["title"]), cards))
    elif t == "end":
        parts.append('<div class="s" id="s%d"><div class="end-bar"></div><h1 class="end-title">%s</h1><div class="end-bar" style="margin-top:1.5em"></div><p class="end-sub">%s</p></div>' % (i, htmlmod.escape(s["title"]), htmlmod.escape(s["subtitle"])))

n = len(SLIDES)
slides_html = "\n".join(parts)

JS = (
    "var s=document.querySelectorAll('.s'),d=document.querySelector('.dots'),p=document.querySelector('.pg'),c=0,n=%d;"
    "for(var i=0;i<n;i++){var x=document.createElement('div');x.className='dot'+(i===0?' active':'');x.style.cursor='pointer';"
    "x.addEventListener('click',(function(j){return function(){g(j)};})(i));d.appendChild(x)}"
    "function g(j){if(j===c)return;s[c].classList.remove('active');if(j>c)s[c].classList.add('prev');"
    "setTimeout(function(){s[c].classList.remove('prev')},400);s[j].classList.add('active');c=j;"
    "for(var k=0;k<d.children.length;k++)d.children[k].classList.toggle('active',k===c);p.textContent=(c+1)+' / '+n};"
    "document.addEventListener('keydown',function(e){"
    "if(e.key==='ArrowRight'||e.key===' '||e.key==='ArrowDown'){e.preventDefault();g(Math.min(c+1,n-1))};"
    "if(e.key==='ArrowLeft'||e.key==='ArrowUp'){e.preventDefault();g(Math.max(c-1,0))}});"
    "var tx=0;document.addEventListener('touchstart',function(e){tx=e.touches[0].clientX},{passive:true});"
    "document.addEventListener('touchend',function(e){var dx=tx-e.changedTouches[0].clientX;"
    "if(dx>50)g(Math.min(c+1,n-1));if(dx<-50)g(Math.max(c-1,0))},{passive:true});"
) % n

HTML = "<!DOCTYPE html>\n<html lang='zh-CN'>\n<head>\n<meta charset='UTF-8'>\n<meta name='viewport' content='width=device-width,initial-scale=1.0'>\n<title>" + htmlmod.escape(TITLE) + "</title>\n<style>" + CSS + "</style>\n</head>\n<body>\n<div class='wrap'><div class='box'>\n" + slides_html + "\n</div></div>\n<div class='dots'></div>\n<div class='pg'>1 / " + str(n) + "</div>\n<script>" + JS + "</script>\n</body>\n</html>"

with open("/workspace/ppts/dist/index.html","w",encoding="utf-8") as f:
    f.write(HTML)
print("OK:", n, "pages,", len(HTML), "bytes")
