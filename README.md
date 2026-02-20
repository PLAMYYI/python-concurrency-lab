# Software-Testing
# Python Concurrency Lab

โปรเจกต์นี้เป็นการทดลองเขียนโปรแกรมโดยใช้ Concurrency ในภาษา Python
เพื่อดูความแตกต่างของการทำงานแต่ละแบบ โดยทดลองใช้ทั้งหมด 3 แบบ คือ
- Thread
- Asyncio
- Process Pool

โครงสร้างไฟล์
- thread_example.py
- asyncio_example.py
- process_pool_example.py

1. Thread Example
โปรแกรมนี้จำลองการดาวน์โหลดไฟล์ 3 ไฟล์พร้อมกัน
โดยใช้ threading.Thread แต่ละ thread จะ sleep 2 วินาที เพื่อจำลองการโหลดข้อมูล
แนวคิด:
Thread เหมาะกับงานประเภท I/O-bound เช่น การอ่านไฟล์ หรือ network
วิธีรัน:
python thread_example.py

2. Asyncio Example
โปรแกรมนี้จำลองการดึงข้อมูลจาก API 3 ตัวพร้อมกัน
ใช้ async/await และ asyncio.gather()
แนวคิด:
Asyncio ใช้ event loop ทำงานแบบ asynchronous
เหมาะกับงาน I/O ที่ต้องรอ เช่น API หรือ network
วิธีรัน:
python asyncio_example.py

3. Process Pool Example
โปรแกรมนี้คำนวณค่า factorial ของตัวเลขหลายตัว
โดยใช้ ProcessPoolExecutor
แนวคิด:
Process Pool เหมาะกับงาน CPU-bound
เช่น งานคำนวณหนัก ๆ เพราะไม่ติด GIL
วิธีรัน:
python process_pool_example.py

สรุปสิ่งที่ได้เรียนรู้
- Thread เหมาะกับงาน I/O แต่ยังติด GIL ถ้าเป็นงานคำนวณหนัก
- Asyncio ใช้ event loop ทำให้ไม่ต้องสร้างหลาย thread
- Process Pool ใช้หลาย process จริง ทำให้เหมาะกับงาน CPU-bound
- แต่ละแบบเหมาะกับงานต่างประเภทกัน
