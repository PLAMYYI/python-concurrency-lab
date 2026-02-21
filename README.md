# Software-Testing
# Python Concurrency Lab

โปรเจกต์นี้เป็นการทดลองเขียนโปรแกรมโดยใช้ Concurrency ในภาษา Python
เพื่อดูความแตกต่างของการทำงานแต่ละแบบ โดยทดลองใช้ทั้งหมด 3 แบบ คือ
- Thread
- Asyncio
- Process Pool

โครงสร้างไฟล์
- python-concurrency-lab
    - thread_example.py
    - asyncio_example.py
    - process_pool_example.py
- tests
    - test_thread.py
    - test_asyncio.py
    - test_process.py
- README.md

1. Thread Example
โปรแกรมคำนวณค่า n² โดยใช้หลาย Thread
แนวคิด : Thread เหมาะกับงานประเภท I/O-bound เช่น การอ่านไฟล์ 
วิธีรัน : python thread_example.py

2. Asyncio Example
โปรแกรมคำนวณค่า n² แบบ asynchronous
โดยใช้ async/await และ asyncio.gather()
แนวคิด : Asyncio ใช้ event loop ทำงานแบบ asynchronous เหมาะกับงาน I/O ที่ต้องรอ เช่น API หรือ network
วิธีรัน : python asyncio_example.py

3. Process Pool Example
โปรแกรมคำนวณค่า กำลังสอง (n²) ของตัวเลขหลายตัว
โดยใช้ ProcessPoolExecutor ให้แต่ละตัวเลขถูกรันใน process แยกกัน
แนวคิด : Process Pool เหมาะกับงาน CPU-bound เช่น งานคำนวณหนัก ๆ เพราะไม่ติด GIL
วิธีรัน : python process_pool_example.py

4.Testing
มีการเขียน Unit Test โดยใช้ unittest และตรวจสอบความครอบคลุมด้วย coverage

ลักษณะของ Test Case
Test ถูกออกแบบให้ครอบคลุม ประกอบด้วย
- Normal Case (ค่าปกติ)
- Boundary Case (ค่า 0 และค่าลบ)
- Multiple Inputs
- Empty List
- Invalid Input (ตรวจสอบ TypeError)
วิธีรัน : python -m unittest discover -s tests
วิธีตรวจสอบ Coverage : 
    - coverage run --source=thread_example,process_pool_example,asyncio_example -m unittest discover -s tests
    - coverage report -m
