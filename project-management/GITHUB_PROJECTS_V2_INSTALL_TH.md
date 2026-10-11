# คู่มือติดตั้ง GitHub Projects v2 แบบ Kanban จริง — AMLO Cybercrime

เอกสารนี้ใช้ Repository เดิม `chaowarojs1-bot/amlo-cybercrime-management-platform` ไม่ใช้ Azure DevOps และไม่สร้าง GitHub Issues ซ้ำ

## สถานะปัจจุบัน

- มีสคริปต์ติดตั้ง [scripts/install_github_project_v2.py](../scripts/install_github_project_v2.py) และ GitHub Actions Workflow แล้ว
- **ยังไม่ถือว่าสร้าง GitHub Projects v2 จริงสำเร็จจนกว่าจะรัน Workflow โหมด install ผ่าน และมีลิงก์ Project ใน Job Summary**
- ตัวติดตั้งตั้ง Project เป็น **Private** และเชื่อมกับ Repository เดิมที่เป็น **Public** ซึ่งยังคงต้องห้ามเผยแพร่ข้อมูลคดีจริง

## ขั้นตอนที่ 1 — สร้าง GitHub Token สำหรับ Projects

1. ใช้บัญชี GitHub ที่มีสิทธิ์เป็นเจ้าของหรือสร้าง Projects ภายใต้ `chaowarojs1-bot`
2. ไปที่ GitHub Settings > Developer settings > Personal access tokens และสร้าง Token ที่มีสิทธิ์ `project` สำหรับ Projects v2; หากนโยบายบัญชีรองรับ Fine-grained Token ให้ใช้สิทธิ์ Projects Read/Write และสิทธิ์อ่าน Issues ที่จำเป็นเท่านั้น
3. กำหนดวันหมดอายุให้สั้นตามความเหมาะสม และ **ไม่ส่ง Token ผ่านแชตหรือใส่ในไฟล์ Repository**
4. เปิดหน้า Repository > Settings > Secrets and variables > Actions > New repository secret
5. ตั้งชื่อ Secret ให้ตรงตัวเป็น `AMLO_PROJECT_TOKEN` และวาง Token ลงในส่วน Secret value

**หมายเหตุ:** Workflow โหมด `validate` ไม่จำเป็นต้องใช้ AMLO_PROJECT_TOKEN เพราะใช้ GITHUB_TOKEN สำหรับตรวจสอบ Issues เท่านั้น

## ขั้นตอนที่ 2 — ทดสอบและติดตั้ง

1. เปิด [Actions: ติดตั้ง GitHub Projects v2 Kanban — AMLO](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/actions/workflows/create-github-project-v2.yml)
2. กด **Run workflow** เลือก `validate` แล้วตรวจผลใน Job Summary ว่าพบ 16 Epics, 75 User Stories, 17 Sprint Trackers, 4 TOR Gates, 4 Governance Issues รวม **116 รายการ**
3. เมื่อผ่านแล้วกด Run workflow อีกครั้ง เลือก `install`
4. รอ Workflow ทำงานสำเร็จ แล้วเปิดลิงก์ Projects v2 ที่แสดงใน **Job Summary**
5. หาก Run แสดง Error เรื่อง Permission ให้ตรวจว่า Token เป็นของเจ้าของบัญชี Project และมี Scope เหมาะสม (ไม่ต้องส่ง Token มาให้ผู้ช่วย)

## ขั้นตอนที่ 3 — ผลลัพธ์หลัง install สำเร็จ

| ส่วน | ผลลัพธ์ |
|---|---|
| GitHub Project | AMLO Cybercrime — Scrum & TOR Kanban (Private) |
| Scrum | Board view `Scrum \| Kanban` กรอง WorkType = User Story |
| Program | Board view `Program \| Epics` กรอง WorkType = Epic |
| Delivery | Board view `Delivery \| TOR` กรอง WorkType = TOR Gate |
| Sprint | Table view `Sprints \| แผน` และฟิลด์ `SprintPlan` S01–S17 |
| ทั้งโครงการ | Table view `All Work \| Master` |
| สถานะ | Product Backlog, Ready, In Progress, Code Review, Testing, PO Review, Done |
| ฟิลด์อื่น | Squad, Priority, TORGate, DeliveryStage, Blocked, StoryPoints, EvidenceRef |
| Issues | เพิ่ม GitHub Issue เดิมเข้า Project เท่านั้น ไม่สร้าง Issues ซ้ำ |

## ขั้นตอนที่ 4 — ตั้งค่ามุมมองครั้งแรก

ใน Scrum Board เลือกเมนูมุมมองและตรวจว่า Layout = Board และ Group by = Status ซึ่งเป็น 7 คอลัมน์ตามที่กำหนด

สำหรับ Delivery Board หากต้องการคอลัมน์กระบวนการตรวจรับโดยเฉพาะ ให้ตั้ง **Group by = DeliveryStage** (Planning, Preparing, Evidence Review, SIT/UAT, Submitted, Accepted, Returned) และบันทึก View; ปัจจุบัน GraphQL API ตั้งค่า Layout และ Filter ได้ แต่การจัดกลุ่มคอลัมน์บางแบบอาจต้องตั้งผ่าน UI

ตั้งค่าการเข้าถึง Project ให้ผู้บริหาร PM, PO, QA และ Developers ที่ได้รับอนุญาตเท่านั้น อย่าเปิด Project เป็น Public โดยไม่ผ่านกระบวนการอนุมัติ

## ความปลอดภัยและการติดตามความคืบหน้า

- `SprintPlan` เป็น **Forecast** จาก Issue เดิม ไม่ใช่ Sprint Commitment และไม่ได้ตั้ง Iteration dates เพราะวันเริ่มสัญญาจริงยังไม่ยืนยัน
- TOR D30/D120/D210/D240 เป็นจุดตรวจรับตามแผน ไม่ใช่หลักฐานการตรวจรับหรือการจ่ายเงิน
- งานที่ปิดใน GitHub ไม่ได้ถูกเปลี่ยนเป็น Done หรือ Accepted โดยอัตโนมัติ
- `StoryPoints` และ `EvidenceRef` ไม่กำหนดค่าเริ่มต้น ต้องใช้ข้อมูลที่ PO/Developers และ PM ยืนยันเท่านั้น
- หาก Workflow ถูกสั่งซ้ำ จะพยายามใช้ Project เดิม ไม่สร้าง Issues ซ้ำ และไม่เขียนทับค่าฟิลด์ที่ทีมใส่ไว้แล้ว
- การสร้าง Project แบบ Private **ไม่ได้เปลี่ยน Repository ต้นทางจาก Public**

## ข้อจำกัดและการแก้ปัญหา

- การติดตั้ง Project ต้องใช้ Token ที่ผู้ใช้จัดเก็บใน GitHub Actions Secret เอง; เครื่องมือ ChatGPT ที่เชื่อมอยู่ไม่สามารถให้สิทธิ์ส่วนนี้แทนได้
- หาก Github API เปลี่ยน Schema หรือสิทธิ์ไม่เพียงพอ Workflow จะหยุดพร้อมข้อความ Error; ก่อนรันซ้ำให้ตรวจขั้นตอนที่ล้มเหลวใน Logs
- หากโครงการสร้างค้างระหว่างทาง สามารถรันโหมด `install` ซ้ำได้หลังแก้ไขเหตุขัดข้อง; ระบบจะไม่คัดลอก Issues เดิม
- **GitHub Projects เป็นระบบหลักสำหรับสถานะงานแบบลากการ์ด**; Markdown Boards ก่อนหน้านี้อ้างสถานะจาก Issue Labels ซึ่งไม่ได้ซิงก์กับ Status ใน Projects โดยอัตโนมัติ

## ลิงก์สำคัญ

- [Workflow ติดตั้ง GitHub Projects v2](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/actions/workflows/create-github-project-v2.yml)
- [Issues ต้นทาง](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues)
- [รูปแบบ Scrum ที่กำหนดไว้](./GITHUB_PROJECT_BOARD_SETUP_PUBLIC.md)
- [Scrum Board แบบ Markdown เดิม](./SCRUM_BOARD.md)
