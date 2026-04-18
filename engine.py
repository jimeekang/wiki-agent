import json
import os
import re
import subprocess
import uuid
from datetime import datetime


class PReinforceEngine:
    INDEX_NAV_HEADER = "## 📂 Navigation"
    INDEX_STATUS_HEADER = "## 🧠 System Status"

    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.meta_dir = os.path.join(root_dir, "20_Meta")
        self.wiki_dir = os.path.join(root_dir, "10_Wiki")
        self.raw_dir = os.path.join(root_dir, "00_Raw")

        self.policy_path = os.path.join(self.meta_dir, "Policy.md")
        self.graph_path = os.path.join(self.meta_dir, "Graph.json")
        self.index_path = os.path.join(self.meta_dir, "Index.md")

        # Current deterministic routing rules for this repository.
        self.routing_rules = [
            {
                "match": ["gstack", "garry tan"],
                "output_dir": ["Topics", "AI_Development", "GStack"],
                "title_prefix": "GStack: ",
                "summary": "GStack는 Garry Tan이 공개한 Claude Code 기반의 역할 중심 에이전트 워크플로우 시스템이다.",
                "tags": [
                    "gstack",
                    "claude-code",
                    "agent-workflow",
                    "role-based-ai",
                    "software-engineering-automation",
                ],
                "confidence": 0.98,
                "related": ["Harness_Engineering", "P_Reinforce_Skill"],
                "policy_update": "Organized GStack related knowledge into Topics/AI_Development/GStack for systemic role-based agent operations.",
                "synthesized": [
                    "범용 AI 대신 CEO, Designer, Eng Manager, QA 등 명확한 전문 역할을 부여해 사고 품질을 높인다.",
                    "단순 코딩보다 /office-hours(문제 정의)와 /plan-eng-review(설계 잠금) 같은 전행 프로세스를 강조한다.",
                    "설계 결과값은 DESIGN.md와 CLAUDE.md에 영속화하여 세션 간 일관성을 유지한다.",
                    "브라우저 기반 검증(/browse), 보안 감사(/cso), 안전장치(/guard)를 통해 에이전트 운영의 안전성을 확보한다.",
                ],
                "contradictions": [
                    "개별 도구(tools)보다는 AI 소프트웨어 팀을 운영하는 '프레임워크'이자 '철학'으로 접근해야 유효하다.",
                ],
            },
            {
                "match": ["p-reinforce"],
                "output_dir": ["Skills"],
                "slug": "P-Reinforce_Skill",
                "title": "P-Reinforce Skill",
                "index_title": "🚀 P-Reinforce Skill",
                "summary": (
                    "P-Reinforce 운영 스킬은 원천 지식을 위키 노트, 그래프, 정책으로 "
                    "승격시키는 실행 패턴을 정의한다."
                ),
                "tags": [
                    "p-reinforce",
                    "rl",
                    "knowledge-automation",
                    "llm-wiki",
                    "github",
                ],
                "confidence": 0.97,
                "related": ["LLM_Wiki_Architecture", "LLM_Wiki_Concepts"],
                "policy_update": (
                    "Added `P-Reinforce Skill` as an executable pattern note "
                    "and reinforced the `Skills` category as a first-class layer."
                ),
                "synthesized": [
                    "Karpathy식 영속적 위키 운영을 RL 정책으로 감싸 분류 정확도, 연결성, 사용자 만족도를 함께 최적화한다.",
                    "`00_Raw/`는 입력 버퍼, `10_Wiki/`는 구조화 지식층, `20_Meta/`는 운영 정책과 그래프 계층으로 사용한다.",
                    "기존 카테고리와 유사도가 높으면 재사용하고, 아니면 새 상위 개념을 생성한다.",
                    "모든 지식 변화는 Git 단위로 추적하며 푸시 성공 여부를 강화 신호로 활용한다.",
                ],
                "contradictions": [
                    "기존 `Topics/AI_Gardening` 문서는 개념 설명 중심이었고, 이 노트는 실제 운영 패턴을 독립된 스킬 계층으로 분리한다.",
                ],
            },
            {
                "match": ["하네스", "harness"],
                "output_dir": ["Topics", "AI_Engineering"],
                "slug": "Harness_Engineering",
                "title": "Harness Engineering",
                "index_title": "🧰 Harness Engineering",
                "summary": (
                    "하네스 엔지니어링은 프롬프트 자체보다 AI가 일하는 운영 환경을 "
                    "설계하는 상위 개념이다."
                ),
                "tags": [
                    "harness-engineering",
                    "ai-systems",
                    "constraints",
                    "feedback-loop",
                    "context-engineering",
                ],
                "confidence": 0.93,
                "related": ["P_Reinforce_Skill", "LLM_Wiki_Architecture"],
                "policy_update": (
                    "Created `Topics/AI_Engineering` for agent operating-environment "
                    "concepts such as harness design."
                ),
                "synthesized": [
                    "시스템 품질은 프롬프트 한 줄보다 모델이 일하는 구조화된 환경의 영향이 더 크다.",
                    "핵심 구성요소는 컨텍스트 엔지니어링, 제약 조건, 피드백 루프, 엔트로피 관리다.",
                    "규칙은 많을수록 좋은 것이 아니라, 실패를 줄이는 최소 집합이어야 한다.",
                    "테스트와 리뷰 같은 외부 검증이 모델의 낮은 자기평가 능력을 보완한다.",
                ],
                "contradictions": [
                    "프롬프트 엔지니어링이 무엇을 말할지의 문제라면, 하네스 엔지니어링은 어떤 환경에서 일하게 할지의 문제다.",
                    "자유도를 늘리면 창의성은 생길 수 있지만, 실무 시스템에서는 제약이 강할수록 정확도와 생산성이 오르는 경우가 많다.",
                ],
            },
            {
                "match": ["이미지", "판독기", "gemma", "estimate"],
                "output_dir": ["Projects", "Painting_Estimate_AI"],
                "slug": "Gemma_Image_Assessment_Estimate_Architecture",
                "title": "Gemma Image Assessment Estimate Architecture",
                "index_title": "🖼️ Estimate Image Architecture",
                "summary": (
                    "이미지 분석은 LLM이 맡되, 가격 산정은 규칙 엔진으로 고정하고 "
                    "최종 확정은 사람이 담당하는 견적 앱 아키텍처다."
                ),
                "tags": [
                    "gemma",
                    "multimodal-llm",
                    "estimate-ai",
                    "price-engine",
                    "case-state",
                ],
                "confidence": 0.95,
                "related": [
                    "Harness_Engineering",
                    "P_Reinforce_Skill",
                    "Local_Agent_Obsidian",
                ],
                "policy_update": (
                    "Created `Projects/Painting_Estimate_AI` for product-specific "
                    "multimodal estimate workflows and rule-engine integrations."
                ),
                "synthesized": [
                    "멀티모달 LLM은 사진에서 손상 후보를 추출하고 설명문을 쓰는 역할에 적합하다.",
                    "안정적인 설계는 photo analysis, case-state update, human confirmation, price engine, summary generation의 다단계 흐름이다.",
                    "LLM 출력은 자유 텍스트보다 고정 JSON schema여야 후속 로직이 안정적이다.",
                    "대화 히스토리를 길게 끌고 가기보다 canonical case-state JSON만 다음 단계로 넘겨야 한다.",
                    "실제 제품 관점에서는 손상명보다 작업 범위(scope)와 가격 엔진 매핑이 더 중요하다.",
                ],
                "contradictions": [
                    "LLM을 최종 손상 판정기와 가격 결정기로 함께 쓰면 시각적 모호성과 환각 때문에 신뢰성이 떨어진다.",
                    "Genkit은 모델 대체재가 아니라 검증과 흐름 제어를 맡는 오케스트레이션 계층으로 보는 것이 맞다.",
                ],
            },
            {
                "match": ["gstack", "garry tan"],
                "output_dir": ["Topics", "AI_Development", "GStack"],
                "title_prefix": "GStack: ",
                "summary": "GStack는 Garry Tan이 공개한 Claude Code 기반의 역할 중심 에이전트 워크플로우 시스템이다.",
                "tags": [
                    "gstack",
                    "claude-code",
                    "agent-workflow",
                    "role-based-ai",
                    "software-engineering-automation",
                ],
                "confidence": 0.98,
                "related": ["Harness_Engineering", "P_Reinforce_Skill"],
                "policy_update": "Organized GStack related knowledge into Topics/AI_Development/GStack for systemic role-based agent operations.",
                "synthesized": [
                    "범용 AI 대신 CEO, Designer, Eng Manager, QA 등 명확한 전문 역할을 부여해 사고 품질을 높인다.",
                    "단순 코딩보다 /office-hours(문제 정의)와 /plan-eng-review(설계 잠금) 같은 전행 프로세스를 강조한다.",
                    "설계 결과값은 DESIGN.md와 CLAUDE.md에 영속화하여 세션 간 일관성을 유지한다.",
                    "브라우저 기반 검증(/browse), 보안 감사(/cso), 안전장치(/guard)를 통해 에이전트 운영의 안전성을 확보한다.",
                ],
                "contradictions": [
                    "개별 도구(tools)보다는 AI 소프트웨어 팀을 운영하는 '프레임워크'이자 '철학'으로 접근해야 유효하다.",
                ],
            },
        ]

    def _read_text(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def _write_text(self, path, content):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)

    def today(self):
        return datetime.now().strftime("%Y-%m-%d")

    def load_graph(self):
        with open(self.graph_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_graph(self, graph):
        with open(self.graph_path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(graph, f, indent=2, ensure_ascii=False)
            f.write("\n")

    def log_policy(self, message):
        bullet = f"- [{self.today()}] {message}"
        content = self._read_text(self.policy_path)
        if bullet not in content:
            self._write_text(self.policy_path, content.rstrip() + "\n" + bullet + "\n")

    def add_to_index(self, title, path):
        link = f"- [[{path}|{title}]]"
        content = self._read_text(self.index_path)
        if link in content:
            return

        marker = f"{self.INDEX_NAV_HEADER}\n"
        if marker not in content:
            raise ValueError("Navigation section not found in index.")
        self._write_text(self.index_path, content.replace(marker, marker + link + "\n", 1))

    def refresh_index_status(self, document_count):
        content = self._read_text(self.index_path)
        status_block = (
            f"{self.INDEX_STATUS_HEADER}\n"
            f"- **Current RL Version:** 1.1.0\n"
            f"- **Total Documents:** {document_count}\n"
            f"- **Last Sync:** {self.today()}\n"
        )
        pattern = re.compile(
            rf"{re.escape(self.INDEX_STATUS_HEADER)}\n(?:- .*\n)+",
            re.MULTILINE,
        )
        updated = pattern.sub(status_block, content, count=1)
        self._write_text(self.index_path, updated)

    def _normalize_text(self, text):
        return re.sub(r"\s+", " ", text).strip().lower()

    def _slugify_raw_title(self, raw_title):
        slug = re.sub(r"[^\w\s-]", "", raw_title, flags=re.UNICODE)
        slug = slug.strip().replace(" ", "_")
        return slug or f"Raw_{uuid.uuid4().hex[:8]}"

    def _extract_title(self, content, fallback):
        for line in content.splitlines():
            stripped = line.strip()
            if stripped.startswith("#"):
                stripped = stripped.lstrip("#").strip()
                stripped = stripped.replace("[[", "").replace("]]", "")
                if stripped:
                    return stripped
        return fallback

    def _extract_bullets(self, content, limit=5):
        bullets = []
        for line in content.splitlines():
            stripped = line.strip()
            if stripped.startswith("- "):
                bullets.append(stripped[2:].strip())
            elif re.match(r"^\d+\.\s+", stripped):
                bullets.append(re.sub(r"^\d+\.\s+", "", stripped))
            if len(bullets) >= limit:
                break
        return bullets

    def _fallback_rule(self, raw_title):
        slug = self._slugify_raw_title(raw_title)
        return {
            "output_dir": ["Topics", "Inbox"],
            "slug": slug,
            "title": raw_title,
            "index_title": f"📝 {raw_title}",
            "summary": f"`{raw_title}` 원천 문서를 기본 Inbox 토픽으로 구조화했다.",
            "tags": ["inbox", "raw-ingest"],
            "confidence": 0.75,
            "related": ["P_Reinforce_Skill"],
            "policy_update": "Routed an unmatched raw note into `Topics/Inbox` for later refinement.",
            "synthesized": [
                "자동 분류 규칙과 강하게 일치하지 않아 임시 Inbox 주제로 보관한다.",
                "후속 연결과 재분류를 위해 원천 문서의 핵심 내용을 요약해 구조화한다.",
            ],
            "contradictions": [
                "명확한 기존 카테고리가 없으므로 임시 보관 후 추후 상위 개념 분리를 검토한다.",
            ],
        }

    def classify_raw(self, raw_file_path, content):
        basename = os.path.splitext(os.path.basename(raw_file_path))[0]
        haystack = self._normalize_text(f"{basename}\n{content[:2000]}")
        for rule in self.routing_rules:
            if any(token.lower() in haystack for token in rule["match"]):
                return dict(rule)
        return self._fallback_rule(basename)

    def _build_note(self, spec, raw_rel_path, content):
        bullets = self._extract_bullets(content)
        synthesized = list(spec["synthesized"])
        if bullets:
            synthesized.extend(bullets[: max(0, 6 - len(synthesized))])

        category_path = "/".join(["10_Wiki"] + spec["output_dir"])
        related_links = ", ".join(f"[[{item}]]" for item in spec["related"])

        lines = [
            "---",
            f"id: {uuid.uuid4()}",
            f'category: "[[{category_path}]]"',
            f"confidence_score: {spec['confidence']:.2f}",
            "tags: [" + ", ".join(spec["tags"]) + "]",
            f"last_reinforced: {self.today()}",
            'github_commit: "uncommitted"',
            "---",
            "",
            f"# [[{spec['title']}]]",
            "",
            "## Summary",
            f"> {spec['summary']}",
            "",
            "## Synthesized Content",
        ]
        lines.extend(f"- {item}" for item in synthesized)
        lines.extend(["", "## Contradictions & Updates"])
        lines.extend(f"- {item}" for item in spec["contradictions"])
        lines.extend(
            [
                "",
                "## Graph",
                f"- Parent: [[10_Wiki/{spec['output_dir'][0]}|{spec['output_dir'][0]}]]",
                f"- Related: {related_links}",
                f"- Raw Source: [[{raw_rel_path.replace(os.sep, '/')}]]",
            ]
        )
        return "\n".join(lines) + "\n"

    def _upsert_graph_node(self, graph, node_id, label, folder):
        for node in graph["nodes"]:
            if node["id"] == node_id:
                node["label"] = label
                node["folder"] = folder
                return
        graph["nodes"].append({"id": node_id, "label": label, "folder": folder})

    def _upsert_graph_edge(self, graph, source, target, edge_type):
        for edge in graph["edges"]:
            if edge["source"] == source and edge["target"] == target and edge["type"] == edge_type:
                return
        graph["edges"].append({"source": source, "target": target, "type": edge_type})

    def _count_structured_documents(self):
        total = 0
        for _, _, files in os.walk(self.wiki_dir):
            total += sum(1 for name in files if name.endswith(".md"))
        return total

    def update_graph(self, note_spec, raw_title, raw_rel_path):
        graph = self.load_graph()
        doc_id = note_spec["slug"]
        raw_id = self._slugify_raw_title(raw_title) + "_Raw"
        folder = "/".join(note_spec["output_dir"])
        raw_folder = os.path.dirname(raw_rel_path).replace(os.sep, "/")

        self._upsert_graph_node(graph, doc_id, note_spec["title"], folder)
        self._upsert_graph_node(graph, raw_id, raw_title, raw_folder)
        self._upsert_graph_edge(graph, doc_id, raw_id, "raw_source")
        for target in note_spec["related"]:
            self._upsert_graph_edge(graph, doc_id, target, "related")

        graph.setdefault("metadata", {})
        graph["metadata"]["last_updated"] = self.today()
        graph["metadata"]["version"] = "1.1"
        self.save_graph(graph)

    def process_raw(self, raw_file_path):
        raw_abs_path = os.path.abspath(raw_file_path)
        raw_rel_path = os.path.relpath(raw_abs_path, self.root_dir)
        print(f"Processing {raw_rel_path}...")

        content = self._read_text(raw_abs_path)
        raw_title = self._extract_title(content, os.path.splitext(os.path.basename(raw_file_path))[0])
        note_spec = self.classify_raw(raw_file_path, content)

        # Dynamic slug and title handling
        slug = note_spec.get("slug") or self._slugify_raw_title(raw_title)
        title = note_spec.get("title")
        if not title:
            prefix = note_spec.get("title_prefix", "")
            title = f"{prefix}{raw_title}"
        
        index_title = note_spec.get("index_title") or f"📝 {title}"

        note_path = os.path.join(self.wiki_dir, *note_spec["output_dir"], f"{slug}.md")

        # Update spec with dynamic values for building the note
        note_spec["title"] = title
        note_spec["slug"] = slug

        self._write_text(note_path, self._build_note(note_spec, raw_rel_path, content))
        note_rel_path = os.path.relpath(note_path, self.root_dir).replace(os.sep, "/")

        self.add_to_index(index_title, note_rel_path)
        self.update_graph(note_spec, raw_title, raw_rel_path)
        self.log_policy(note_spec["policy_update"])
        self.refresh_index_status(self._count_structured_documents())
        return note_path

    def process_all_raw(self):
        processed = []
        for current_root, _, files in os.walk(self.raw_dir):
            for name in sorted(files):
                if name.endswith(".md"):
                    processed.append(self.process_raw(os.path.join(current_root, name)))
        return processed

    def reinforce_sync(self, action_summary):
        try:
            subprocess.run(["git", "add", "."], cwd=self.root_dir, check=True)
            subprocess.run(["git", "commit", "-m", f"[P-Reinforce] {action_summary}"], cwd=self.root_dir, check=True)
            # subprocess.run(["git", "push", "origin", "main"], cwd=self.root_dir)  # Disabled for local safety
            return True
        except Exception as e:
            print(f"Git sync failed: {e}")
            return False


if __name__ == "__main__":
    engine = PReinforceEngine(".")
    processed = engine.process_all_raw()
    print(f"P-Reinforce Engine Loaded. Processed {len(processed)} raw notes.")
