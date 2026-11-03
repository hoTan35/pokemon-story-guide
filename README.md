# 포켓몬 스토리 공략 도우미

> **PR 제목:** `<type>: <작업 요약>` 형식으로 작성해 주세요.
>
> 예: `feat: 포켓몬 목록 화면 구현` · `fix: 출현 장소 필터 오류 수정`
>
> 브랜치·리뷰 규칙은 [기여 안내](CONTRIBUTING.md)를 참고하세요.

포켓몬스터 하트골드 기준으로 장소별 출현 포켓몬, 포켓몬 상세 정보, 체육관 관장 및 사천왕 공략 정보를 제공하는 팀 프로젝트입니다.

## 저장소 구조

```text
frontend/          프론트엔드 화면
backend/api/       서버 및 API
backend/algorithm/ 상성 및 추천 점수 계산
backend/ai/        AI 기능 및 모델 연동
data/              하트골드 데이터와 초기 JSON
docs/              기능 명세, API 계약, 회의 결정
```

## 브랜치 흐름

- `main`: 제출·시연 가능한 안정 버전
- `develop`: 기능 통합 브랜치
- `feature/*`, `fix/*`: `develop`에서 분기하고 작업 후 PR로 병합
- `release/*`, `hotfix/*`: 필요할 때만 생성

`main`과 `develop`에는 직접 push하지 않고 PR을 통해 병합합니다. PR은 작성자가 아닌 팀원 1명의 승인을 받은 뒤 병합합니다.

## 작업 시작

```bash
git switch develop
git pull
git switch -c feature/작업-이름
```

작업을 마치면 원격에 브랜치를 push하고 `develop`을 대상으로 Pull Request를 생성하세요.

## 보안

비밀 키, 토큰, `.env` 파일은 저장소에 커밋하지 마세요. 필요한 환경 변수는 `.env.example`에 키 이름과 예시 값만 기록합니다.
