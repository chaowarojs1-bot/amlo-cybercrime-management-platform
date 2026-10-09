# ทะเบียนรายการงานผลิตภัณฑ์ (Product Backlog)

รายการนี้เป็นดัชนีสำหรับติดตามงาน สถานะจริงให้ดูที่ GitHub Issues ทั้งนี้ลำดับความสำคัญและ Sprint ยังเป็นข้อเสนอเพื่อให้ Product Owner และ Developers ยืนยัน

| Epic | ระบบหรือสายงาน | User Stories | ลำดับเบื้องต้น |
|---|---|---|---|
| [#5](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/5) | ระบบเข้าสู่ระบบและกำหนดสิทธิ์ | IAM-01 ถึง IAM-04 | P0 |
| [#6](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/6) | ตั้งค่าระบบ | CFG-01 ถึง CFG-04 | P1 |
| [#7](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/7) | แจ้งเตือน | NOT-01 ถึง NOT-04 | P1 |
| [#8](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/8) | เชื่อมโยงข้อมูลและ OCR | INT-01 ถึง INT-05 | P0 |
| [#9](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/9) | วิเคราะห์ธุรกรรมและกราฟ | TXN-01 ถึง TXN-05 | P0 |
| [#10](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/10) | จัดการคดี | CASE-01 ถึง CASE-05 | P0 |
| [#11](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/11) | รับคำร้อง | CLM-01 ถึง CLM-05 | P0 |
| [#12](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/12) | คืนและจัดสรรทรัพย์สิน | REF-01 ถึง REF-05 | P0 |
| [#13](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/13) | ระบบสนทนาอัตโนมัติ | BOT-01 ถึง BOT-04 | P1 |
| [#14](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/14) | รายงาน | RPT-01 ถึง RPT-04 | P1 |
| [#15](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/15) | แดชบอร์ด | DASH-01 ถึง DASH-04 | P1 |
| [#16](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/16) | Cloud และ DevOps | OPS-01 ถึง OPS-05 | P0 |
| [#17](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/17) | ความปลอดภัย ความเป็นส่วนตัว และการตรวจสอบ | SEC-01 ถึง SEC-05 | P0 |
| [#18](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/18) | คุณภาพ ทดสอบ และเผยแพร่ระบบ | QA-01 ถึง QA-06 | P0 |
| [#19](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/19) | ประสบการณ์ผู้ใช้และต้นแบบ | UX-01 ถึง UX-04 | P1 |
| [#20](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/20) | Scrum และกำกับ TOR | GOV-01 ถึง GOV-06 | P0 |

## หลักการจัดลำดับงาน
- Product Owner เป็นผู้จัดลำดับตามคุณค่า ความเสี่ยง และความพร้อมของงานที่ต้องพึ่งพา
- Developers ประเมิน Story Points ระหว่าง Refinement โดยไม่กำหนดค่าขึ้นเอง
- Sprint ที่ระบุใน Issues เป็นเพียงการคาดการณ์ ไม่ใช่คำมั่นของ Sprint
- การตัดสินใจทางกฎหมายและกฎการคืนทรัพย์สินต้องได้รับการยืนยันจากผู้มีอำนาจ
- เอกสารเชื่อมโยง TOR รายข้อและหลักฐานลับต้องจัดเก็บในระบบควบคุมสิทธิ์

## การจัดการข้อมูลซ้ำ
Issues #41–#43 ถูกปิดเป็นรายการซ้ำของ TXN-01 ถึง TXN-03 โดยใช้ #38–#40 เป็นรายการหลัก

## สถานะงาน
Product Backlog → Ready → In Progress → Code Review → Testing → PO Review → Done

**การตรวจรับตาม TOR แยกต่างหากจากสถานะ Done**
