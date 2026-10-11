# โครงการระบบบริหารจัดการอาชญากรรมทางเทคโนโลยี ปปง.

คลังเอกสารแผนงานฉบับเปิดเผยได้ของโครงการ AMLO Cybercrime Management Platform

> **ข้อควรระวัง:** คลังนี้เป็นสาธารณะ ห้ามเผยแพร่ข้อมูลผู้เสียหาย ข้อมูลคดี บัญชีธนาคาร หลักฐานจริง รหัสผ่าน ระบบเครือข่ายภายใน หรือผลการตรวจสอบช่องโหว่

## กระดานหลัก: GitHub Projects v2 แบบ Kanban (Public)

**[เปิด AMLO Cybercrime — Scrum & TOR Kanban (Project #1)](https://github.com/users/chaowarojs1-bot/projects/1)**

- กระดานหลัก **Public** รักษา URL เดิมสำหรับ QR Code และใช้ GitHub Issues ชุดเดิม **116 รายการ**
- ย้ายข้อมูลจาก [Project #2](https://github.com/users/chaowarojs1-bot/projects/2) แล้ว โดยคง Project #2 เป็น Private และไม่แก้ไขต้นทาง
- มี **6 มุมมอง** ตามโครงสร้างจาก Project #2 ได้แก่ Scrum, Program, Delivery, Sprints, All Work และ View 1
- Draft Issues เดิม 12 รายการของ Project #1 ถูกเก็บใน Archive และสำรองไว้ใน [Project #3 (Private)](https://github.com/users/chaowarojs1-bot/projects/3)
- [ผลการย้ายที่สำเร็จใน GitHub Actions](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/actions/runs/38131158150)

**ข้อควรทราบ:** GitHub Projects คือกระดานบริหารงานหลัก ไม่ใช่ Markdown Board; ค่า Status ใน Projects ไม่ได้ซิงก์กับ Labels ของ Issues โดยอัตโนมัติ ต้องตรวจการตั้งค่า Group by/Sort และสิทธิ์การเข้าถึงแต่ละ View ตามการใช้งานจริง

## เปิดกระดานบริหารงานบน GitHub

- **[Scrum Board — กระดานพัฒนา 75 User Stories](./project-management/SCRUM_BOARD.md)**
- **[Program Board — ภาพรวม 16 Epics](./project-management/PROGRAM_BOARD.md)**
- **[Delivery Board — ตรวจรับ TOR 4 งวด และ Sprint 17 รอบ](./project-management/DELIVERY_BOARD.md)**
- [คู่มือเปลี่ยนสถานะและซิงก์กระดานฉบับภาษาไทย](./project-management/BOARD_USER_GUIDE_TH.md)

กระดานเหล่านี้เป็นหน้าบน GitHub Repository ที่สร้างจาก GitHub Issues เดิม ไม่ใช่ GitHub Projects v2 แบบลากการ์ด ระบบซิงก์ผ่าน GitHub Actions เมื่อเปิดใช้งานและรัน Workflow

## กรอบการดำเนินงาน
- ระยะเวลาตามแผน TOR: **240 วันปฏิทิน**
- จุดส่งมอบตามสัญญา: วันที่ 30, 120, 210 และ 240
- วันที่ 1 ตุลาคม 2569 เป็น **วันเริ่มต้นสมมติสำหรับวางแผน** ยังไม่ใช่วันที่เริ่มสัญญาที่ได้รับการยืนยัน
- ใช้ **Scrum สำหรับการพัฒนา** ควบคู่กับการควบคุมการส่งมอบตาม TOR
- การกำหนด Product Owner, บุคลากร, Story Points และ Sprint Goal ต้องผ่านการยืนยันของผู้รับผิดชอบ

## ศูนย์รวมเอกสาร Scrum
1. [กระดานภาพรวมโครงการ](./project-management/PROGRAM_MASTER_BOARD_PUBLIC.md)
2. [ทะเบียน Sprint ทั้ง 17 รอบ](./project-management/SPRINT_ISSUE_REGISTER_PUBLIC.md)
3. [รูปแบบการทำงาน Scrum และบทบาททีม](./project-management/SCRUM_OPERATING_MODEL_PUBLIC.md)
4. [ทะเบียน Product Backlog](./project-management/PRODUCT_BACKLOG_REGISTER_PUBLIC.md)
5. [แผน Sprint Roadmap](./project-management/SPRINT_ROADMAP_PUBLIC.md)
6. [นิยามความพร้อมและความสำเร็จของงาน](./project-management/DEFINITION_OF_READY_DONE_PUBLIC.md)
7. [ความสัมพันธ์ระหว่างงานและความเสี่ยง](./project-management/DEPENDENCY_RISK_REGISTER_PUBLIC.md)
8. [การตรวจรับงานตาม TOR](./project-management/RELEASE_ACCEPTANCE_PUBLIC.md)
9. [การประชุม Scrum และตัวชี้วัด](./project-management/SCRUM_CEREMONIES_METRICS_PUBLIC.md)
10. [การเชื่อมโยง TOR กับ Backlog](./project-management/TOR_TRACEABILITY_PUBLIC.md)
11. [แนวทางตั้งค่า GitHub Projects](./project-management/GITHUB_PROJECT_BOARD_SETUP_PUBLIC.md)

## รายการงานที่สร้างแล้ว
- Epic 16 รายการ ครอบคลุม 11 ระบบตาม TOR และงานสนับสนุน
- User Story 75 รายการ พร้อมเกณฑ์ยอมรับเบื้องต้น
- Sprint Tracker 17 รายการ (เป็นแผน ไม่ใช่ Sprint ที่เริ่มดำเนินการแล้ว)
- จุดตรวจรับ TOR 4 รายการ: [วันที่ 30](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/99), [วันที่ 120](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/100), [วันที่ 210](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/101), [วันที่ 240](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/102)
- [เปิดรายการงาน GitHub Issues](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues)

## สถานะกระดานบน GitHub
**สร้าง GitHub Projects v2 แบบ Kanban จริงแล้ว** ที่ [Project #1 (Public)](https://github.com/users/chaowarojs1-bot/projects/1) พร้อม 116 Issues และ 6 มุมมอง ส่วน Markdown Boards ยังเก็บไว้เป็นรายงานประกอบซึ่งไม่ซิงก์สองทางกับ Status ของ Projects

## เอกสารเดิม
- [แผนบริหารโครงการ](./project-management/PROJECT_MASTER_PLAN_PUBLIC.md)
- [แผนดำเนินงาน](./roadmap/ROADMAP.md)
- [สรุป TOR](./docs/TOR_SUMMARY_PUBLIC.md)
- [ภาพรวมสถาปัตยกรรม](./architecture-public/ARCHITECTURE_OVERVIEW.md)

**หลักการสำคัญ:** การปิด Issue ไม่เท่ากับการตรวจรับตามสัญญา การทดสอบ SIT/UAT และการลงนามตรวจรับยังต้องดำเนินการตามขั้นตอนอย่างเป็นทางการ
