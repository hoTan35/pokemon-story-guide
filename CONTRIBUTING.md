# 기여 규칙

## 브랜치

- 작업 전 최신 `develop`을 가져와서 새 브랜치를 만듭니다.
- 기능: `feature/<영역>-<작업>` (예: `feature/frontend-pokemon-list`)
- 수정: `fix/<영역>-<작업>` (예: `fix/api-encounter-filter`)
- 문서: `docs/<작업>` (예: `docs/setup-guide`)
- 일반 작업 PR은 `develop`을 대상으로 하고, 릴리스 PR만 `main`을 대상으로 합니다.

## PR 제목

`<type>: <작업 요약>` 형식으로 작성합니다.

- `feat`: 기능 추가
- `fix`: 오류 수정
- `docs`: 문서 변경
- `refactor`: 구조 개선
- `test`: 테스트 변경
- `chore`: 설정·기타 작업

예: `feat: 포켓몬 목록 화면 구현`, `fix: 출현 장소 필터 오류 수정`

## 리뷰와 병합

- `main`과 `develop`에는 직접 푸시하거나 강제 푸시하지 않고 PR로 병합합니다.
- 작성자 외 팀원 1명의 승인을 받은 뒤 병합합니다.
- 리뷰 대화는 해결한 뒤 병합합니다.
- 병합되면 작업 브랜치는 자동 삭제됩니다.
