# คู่มือจัดตั้งกระดาน GitHub Projects สำหรับ Scrum

**สถานะ:** เป็นข้อกำหนดสำหรับการตั้งค่าเท่านั้น ยังไม่ได้สร้างกระดาน Projects v2 พร้อมฟิลด์และระบบอัตโนมัติจริง

## ชื่อกระดานที่เสนอ
**AMLO Cybercrime — Program Scrum**

## ฟิลด์ที่ต้องตั้งค่า
| ฟิลด์ | ประเภท | ค่าแนะนำ |
|---|---|---|
| Status | ตัวเลือกเดียว | Product Backlog, Ready, In Progress, Code Review, Testing, PO Review, Done |
| Type | ตัวเลือกเดียว | Epic, Story, Task, Bug, Enabler, Gate |
| Squad | ตัวเลือกเดียว | A, B, C, D, E, Shared, Cross-team |
| Priority | ตัวเลือกเดียว | P0, P1, P2, P3 |
| Sprint | รอบการทำงาน | รอบละสองสัปดาห์ ปรับตามวันเริ่มจริง |
| Target Gate | ตัวเลือกเดียว | D30, D120, D210, D240, ไม่เกี่ยวข้อง |
| Story Points | ตัวเลข | ให้ Developers ประเมิน |
| Blocked | ตัวเลือกเดียว | Yes, No |
| Blocked Since | วันที่ | ระบุเมื่อมีอุปสรรค |
| Owner | ผู้รับผิดชอบ | กำหนดหลังยืนยันทีม |
| Dependency Reference | ข้อความ | รหัส Issue หรือการพึ่งพา |
| Evidence/RTM Reference | ข้อความ | รหัสหลักฐานที่เปิดเผยได้ |

## มุมมองที่แนะนำ
1. **Program Master Board:** แสดงงานตาม Status
2. **Product Backlog:** ตารางลำดับงานที่ Product Owner ดูแล
3. **Squad A–E:** แยกมุมมองตามสายงาน
4. **Current Sprint:** งานและเป้าหมายของ Sprint ปัจจุบัน
5. **Dependency Watch:** งานที่ถูก Blocked และผู้รับผิดชอบ
6. **Release & TOR Gate:** สถานะหลักฐานแต่ละงวด
7. **Quality & Security:** ผลทดสอบในระดับที่เปิดเผยได้
8. **Executive Overview:** ภาพรวมงาน ความเสี่ยง และความพร้อมตรวจรับ

## แนวทางตั้งค่า
1. ผู้ดูแล GitHub สร้าง Project ภายใต้บัญชีเจ้าของ Repository
2. เพิ่ม Issues ที่มีอยู่ลง Project
3. สร้างฟิลด์และมุมมองตามตาราง
4. กำหนดสิทธิ์ให้ Product Owner จัดลำดับและทีมดูแลสถานะ
5. ตั้ง Iteration ตามวันเริ่มสัญญาที่ได้รับการยืนยัน
6. เชื่อมกระบวนการ Pull Request กับ Code Review/Testing ตามความเหมาะสม
7. ปิดงานเมื่อผ่าน Definition of Done เท่านั้น
8. ตรวจรับ TOR แยกจากการปิด Issue

ห้ามใส่ข้อมูลจริงของคดีหรือรายละเอียดความปลอดภัยที่เป็นความลับในฟิลด์ข้อความ
