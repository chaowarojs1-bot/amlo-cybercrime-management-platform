# คู่มือใช้งานกระดาน Scrum บน GitHub — AMLO Cybercrime

> กระดานนี้แสดงผลเป็น Markdown จาก GitHub Issues ไม่ใช่ GitHub Projects v2 แบบลากการ์ด
> Repository เป็นสาธารณะ ห้ามใส่ข้อมูลคดีจริง ข้อมูลผู้เสียหาย ข้อมูลบัญชี หรือข้อมูลความมั่นคง/ช่องโหว่

## 1) เปิดกระดาน

- [Scrum Board](./SCRUM_BOARD.md) — User Stories และสถานะงาน
- [Program Board](./PROGRAM_BOARD.md) — 16 Epics
- [Delivery Board](./DELIVERY_BOARD.md) — TOR Gates และ Sprint Trackers
- [รายการ Issues ทั้งหมด](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues)

## 2) เปลี่ยนสถานะงานด้วย GitHub Labels

ในหน้า Issue ให้เลือก Labels แล้วกำหนด Label สถานะเพียง 1 ค่า ดังนี้

| Label | ความหมาย |
|---|---|
| status:backlog | Product Backlog — ยังไม่เลือกเข้า Sprint |
| status:ready | Ready — ผ่านการเตรียมพร้อมตามข้อตกลงของทีม |
| status:in-progress | In Progress — กำลังพัฒนา |
| status:code-review | Code Review — รอ/กำลังตรวจโค้ด |
| status:testing | Testing — รอ/กำลังทดสอบ |
| status:po-review | PO Review — รอ Product Owner ตรวจ |
| status:done | Done — ผ่าน Definition of Done ตามเกณฑ์ทีม |
| status:blocked | แสดงว่าเป็นอุปสรรค เพิ่มควบคู่กับ Label สถานะได้ |

ไม่ควรติด Label สถานะมากกว่า 1 ค่าใน Issue เดียวกัน หากยังไม่มี Label สถานะและ Issue ยังเปิดอยู่ ระบบจะแสดงเป็น Product Backlog

## 3) แยกกระบวนการส่งมอบ TOR จาก Scrum

ใช้ Label บน Gate Issues #99–#102 อย่างระมัดระวัง:

| Label | ความหมาย |
|---|---|
| gate:preparing | เตรียมชุดส่งมอบ |
| gate:evidence-review | ตรวจความครบถ้วนของหลักฐาน |
| gate:sit-uat | ตรวจหลักฐาน SIT/UAT ตามงวดที่เกี่ยวข้อง |
| gate:submitted | ส่งเพื่อขอตรวจรับ |
| gate:accepted | ตรวจรับแล้ว ต้องมีหลักฐานอนุมัติจริง |
| gate:returned | ส่งกลับเพื่อแก้ไข |

ห้ามใช้ Label gate:accepted โดยยังไม่มีหลักฐานตรวจรับที่ได้รับอนุมัติตามอำนาจหน้าที่ แม้ Issue จะปิดแล้วก็ตาม

## 4) เปิดระบบซิงก์อัตโนมัติ

1. เปิดแท็บ Actions ของ Repository และเลือก Workflow ชื่อ อัปเดตกระดาน AMLO Scrum
2. เลือก Run workflow เพื่อให้ระบบสร้าง Labels ที่ยังไม่มี และอัปเดต Markdown Boards จาก Issues
3. Workflow มีกำหนดทำงานทุกวันเวลา 08:15 น. ตามเวลาประเทศไทย (01:15 UTC) เมื่อ GitHub Actions เปิดใช้งาน
4. หากระบบรายงาน Permission denied หรือ git push ไม่สำเร็จ ให้ผู้ดูแลตรวจที่ Settings > Actions > General > Workflow permissions และกำหนดสิทธิ์ที่จำเป็นตามนโยบายองค์กร
5. เมื่อต้องการดูสถานะล่าสุดโดยไม่รอรอบรายวัน ให้เปิด Workflow แล้วสั่ง Run workflow อีกครั้ง

ไฟล์ตั้งค่า: [.github/workflows/sync-scrum-boards.yml](../.github/workflows/sync-scrum-boards.yml) และสคริปต์ [scripts/sync_boards.py](../scripts/sync_boards.py)

## 5) ข้อจำกัดที่ต้องทราบ

- กระดาน Markdown นี้แสดงข้อมูลที่ซิงก์ล่าสุด ไม่ใช่กระดานลาก-วางของ GitHub Projects v2
- ยังไม่ได้สร้าง Native GitHub Projects v2 เนื่องจากเครื่องมือเชื่อมต่อปัจจุบันไม่รองรับสร้าง Project
- ไม่มีการแก้ไขเนื้อหา Acceptance Criteria และไม่มีการย้ายหรือคัดลอก Issues
- Sprint S01–S17 ยังคงเป็นแผนเสนอ ต้องยืนยันวันเริ่มสัญญา Sprint Goal และความพร้อมของทีม
- ไม่ควรใช้จำนวน Issue ที่ปิดแล้วเป็นหลักฐานยืนยันงานเสร็จหรือการตรวจรับตาม TOR

## 6) หากต้องการ GitHub Projects Board แบบลากการ์ดจริง

เจ้าของ Repository เปิดแท็บ Projects > New project > Board แล้วนำ Issues เดิมทั้งหมดเข้า Project และตั้งฟิลด์ Status ตามคู่มือนี้ หรือใช้ ChatGPT Work ที่เข้าถึงหน้าเว็บ GitHub หลังได้รับการอนุญาตจากเจ้าของบัญชี
