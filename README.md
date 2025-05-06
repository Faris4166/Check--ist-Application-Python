<img src = "BG.jpg">

# Simple Checklist Application in Python (Thai/English) 📝

## คำอธิบาย (Description) ℹ️

This project is a simple checklist application built using Python's Tkinter library for creating the graphical user interface (GUI). It allows users to **add (+)**, **remove (❌)**, and **clear (🗑️)** items from a list, as well as **save (💾)** and **load (📂)** the list to/from a file. The code is structured into logical sections for easy understanding.

โปรเจกต์นี้เป็นแอปพลิเคชันบันทึกรายการตรวจสอบอย่างง่ายที่สร้างด้วยไลบรารี Tkinter ของ Python สำหรับสร้างส่วนติดต่อผู้ใช้แบบกราฟิก (GUI). ผู้ใช้สามารถ**เพิ่ม (+)**, **ลบ (❌)**, และ**ล้าง (🗑️)** รายการจากรายการได้ รวมถึง**บันทึก (💾)** และ**โหลด (📂)** รายการไปยัง/จากไฟล์. โค้ดถูกจัดโครงสร้างเป็นส่วนต่างๆ ที่เข้าใจง่าย.

## โครงสร้างโค้ด (Code Structure) 🧱

The code is organized into the following main sections:

โค้ดถูกจัดระเบียบเป็นส่วนหลักๆ ดังนี้:

### ส่วนที่ 1: นำเข้าและตั้งค่าหน้าต่างหลัก (Part 1: Import and Set Up the Main Window) ⚙️

* Imports necessary modules from the Tkinter library (`tkinter` as `Tk` for GUI elements, `filedialog` for file operations).
* Creates the main window (`root`) and sets its title, icon (if `check.ico` exists), initial size and position, and resizability.
* Defines a font (`Kanit`, size 10) and a background color (`pink`) for the application.

* นำเข้าโมดูลที่จำเป็นจากไลบรารี Tkinter (`tkinter` เป็น `Tk` สำหรับองค์ประกอบ GUI, `filedialog` สำหรับการจัดการไฟล์).
* สร้างหน้าต่างหลัก (`root`) และตั้งค่าชื่อ, ไอคอน (ถ้ามีไฟล์ `check.ico`), ขนาดและตำแหน่งเริ่มต้น, และการอนุญาตให้ปรับขนาด.
* กำหนดฟอนต์ (`Kanit`, ขนาด 10) และสีพื้นหลัง (`pink`) สำหรับแอปพลิเคชัน.

### ส่วนที่ 2: ฟังก์ชันการทำงาน (Part 2: Functionality) 🧠

* **`addItem()`: +** Retrieves text from the `inputEntry` widget and adds it to the `Listbox` if it's not empty after stripping whitespace. Clears the `inputEntry` after adding.
* **`removeItem()`: ❌** Deletes the currently selected item from the `Listbox`.
* **`clearList()`: 🗑️** Deletes all items from the `Listbox`.
* **`saveList()`: 💾** Opens a "save as" dialog using `filedialog.asksaveasfilename(...)`. If a file path is selected, it opens the file in write mode (`"w"` with UTF-8 encoding) and writes each item from the `Listbox` to a new line in the file. **Note:** The actual implementation for writing to the file (`...`) is missing in the provided code snippet.
* **`loadList()`: 📂** Opens an "open" dialog using `filedialog.askopenfilename(...)`. If a file path is selected, it first clears all existing items in the `Listbox`, then opens the file in read mode (`"r"` with UTF-8 encoding), reads each line, removes leading/trailing whitespace using `.strip()`, and inserts it into the `Listbox`. **Note:** The actual implementation for reading from the file (`...`) is missing in the provided code snippet.

* **`addItem()`: +** ดึงข้อความจาก widget `inputEntry` และเพิ่มลงใน `Listbox` หากข้อความนั้นไม่ว่างหลังจากการตัดช่องว่าง. ล้างข้อความใน `inputEntry` หลังจากเพิ่มแล้ว.
* **`removeItem()`: ❌** ลบรายการที่ถูกเลือกอยู่ในปัจจุบันออกจาก `Listbox`.
* **`clearList()`: 🗑️** ลบทุกรายการออกจาก `Listbox`.
* **`saveList()`: 💾** เปิดกล่องโต้ตอบ "บันทึกเป็น" โดยใช้ `filedialog.asksaveasfilename(...)`. หากมีการเลือกพาธไฟล์, จะเปิดไฟล์ในโหมดเขียน (`"w"` ด้วยการเข้ารหัส UTF-8) และเขียนแต่ละรายการจาก `Listbox` ลงในไฟล์ทีละบรรทัด. **หมายเหตุ:** ส่วนของการเขียนข้อมูลลงไฟล์จริงๆ (`...`) ขาดหายไปในโค้ดที่ให้มา.
* **`loadList()`: 📂** เปิดกล่องโต้ตอบ "เปิด" โดยใช้ `filedialog.askopenfilename(...)`. หากมีการเลือกพาธไฟล์, จะล้างรายการทั้งหมดที่มีอยู่ใน `Listbox` ก่อน, จากนั้นเปิดไฟล์ในโหมดอ่าน (`"r"` ด้วยการเข้ารหัส UTF-8), อ่านแต่ละบรรทัด, ตัดช่องว่างหน้าหลังด้วย `.strip()`, และแทรกลงใน `Listbox`. **หมายเหตุ:** ส่วนของการอ่านข้อมูลจากไฟล์จริงๆ (`...`) ขาดหายไปในโค้ดที่ให้มา.

### ส่วนที่ 3: การจัดวาง (Frames) (Part 3: Layout (Frames)) 📐

* Creates three `Frame` widgets (`input_frame`, `output_frame`, `button_frame`) with the specified background color.
* Uses the `pack()` layout manager to arrange these frames vertically with some vertical padding (`pady=10`).
* **Summary:** Frames are used to organize different sections of the window:
    1.  `input_frame`: Holds the input field and buttons for adding/opening files.
    2.  `output_frame`: Displays the list of items (`Listbox`).
    3.  `button_frame`: Contains buttons for managing the list.

* สร้างสาม widget `Frame` (`input_frame`, `output_frame`, `button_frame`) ด้วยสีพื้นหลังที่กำหนด.
* ใช้ตัวจัดการการจัดวาง `pack()` เพื่อจัดเรียงเฟรมเหล่านี้ในแนวตั้งโดยมีระยะห่างแนวตั้ง (`pady=10`).
* **สรุป:** ใช้ Frame เพื่อแบ่งส่วนต่างๆ ของหน้าต่าง เช่น:
    1.  `input_frame`: บรรจุช่องกรอกข้อความและปุ่มสำหรับเพิ่ม/เปิดไฟล์.
    2.  `output_frame`: แสดงรายการ (`Listbox`).
    3.  `button_frame`: บรรจุปุ่มสำหรับจัดการรายการ.

### ส่วนที่ 4: ส่วนรับข้อมูล (Part 4: Input Area) ⌨️

* Creates an `Entry` widget (`inputEntry`) within the `input_frame` for users to type in new items. It has a specified width and font.
* Creates two `Button` widgets within the `input_frame`:
    * `btnOpen`: Labeled "เปิดไฟล์" (Open File) and calls the `loadList` function when clicked.
    * `btnAdd`: Labeled "เพิ่มรายการ" (Add Item) and calls the `addItem` function when clicked.
* Uses the `grid()` layout manager to arrange these widgets in a row within the `input_frame`. **Note:** The specific `grid()` arguments (like `row`, `column`, `padx`, `pady`) are incomplete (`...`).

* สร้าง widget `Entry` (`inputEntry`) ภายใน `input_frame` สำหรับให้ผู้ใช้พิมพ์รายการใหม่. มีการกำหนดความกว้างและฟอนต์.
* สร้างสอง widget `Button` ภายใน `input_frame`:
    * `btnOpen`: มีป้ายกำกับว่า "เปิดไฟล์" (Open File) และเรียกฟังก์ชัน `loadList` เมื่อคลิก.
    * `btnAdd`: มีป้ายกำกับว่า "เพิ่มรายการ" (Add Item) และเรียกฟังก์ชัน `addItem` เมื่อคลิก.
* ใช้ตัวจัดการการจัดวาง `grid()` เพื่อจัดเรียง widget เหล่านี้ในแถวเดียวภายใน `input_frame`. **หมายเหตุ:** อาร์กิวเมนต์เฉพาะของ `grid()` (เช่น `row`, `column`, `padx`, `pady`) ไม่สมบูรณ์ (`...`).

### ส่วนที่ 5: แสดงรายการ (Part 5: Display List) 📜

* Creates a `Listbox` widget (`Listbox`) within the `output_frame` to display the list of items. It has a specified width, height, and font.
* Uses the `grid()` layout manager to place the `Listbox` within the `output_frame`. **Note:** The specific `grid()` arguments are incomplete (`...`).
* **Summary:** This list box is used to show the items added by the user, such as a To-do list.

* สร้าง widget `Listbox` (`Listbox`) ภายใน `output_frame` เพื่อแสดงรายการ. มีการกำหนดความกว้าง, ความสูง, และฟอนต์.
* ใช้ตัวจัดการการจัดวาง `grid()` เพื่อวาง `Listbox` ภายใน `output_frame`. **หมายเหตุ:** อาร์กิวเมนต์เฉพาะของ `grid()` ไม่สมบูรณ์ (`...`).
* **สรุป:** กล่องรายการนี้ใช้เพื่อแสดงสิ่งที่ผู้ใช้เพิ่มเข้ามา เช่น รายการสิ่งที่ต้องทำ.

### ส่วนที่ 6: ปุ่มคำสั่งต่างๆ (Part 6: Command Buttons) 🖱️

* Creates four `Button` widgets within the `button_frame`:
    * `btnRemove`: Calls the `removeItem` function when clicked.
    * `btnClear`: Calls the `clearList` function when clicked.
    * `btnSave`: Calls the `saveList` function when clicked.
    * `btnQuit`: Calls the `root.destroy` method to close the application when clicked.
* Uses the `grid()` layout manager to arrange these buttons in two rows. **Note:** The specific `grid()` arguments and the text labels for these buttons are incomplete (`...`).
    * Row 0: Likely for "ลบ" (Remove), "ล้าง" (Clear), "บันทึก" (Save).
    * Row 1: Likely for "ปิดโปรแกรม" (Quit Program).

* สร้างสี่ widget `Button` ภายใน `button_frame`:
    * `btnRemove`: เรียกฟังก์ชัน `removeItem` เมื่อคลิก.
    * `btnClear`: เรียกฟังก์ชัน `clearList` เมื่อคลิก.
    * `btnSave`: เรียกฟังก์ชัน `saveList` เมื่อคลิก.
    * `btnQuit`: เรียกเมธอด `root.destroy` เพื่อปิดแอปพลิเคชันเมื่อคลิก.
* ใช้ตัวจัดการการจัดวาง `grid()` เพื่อจัดเรียงปุ่มเหล่านี้ในสองแถว. **หมายเหตุ:** อาร์กิวเมนต์เฉพาะของ `grid()` และป้ายกำกับข้อความสำหรับปุ่มเหล่านี้ไม่สมบูรณ์ (`...`).
    * แถว 0: น่าจะเป็นสำหรับ "ลบ" (Remove), "ล้าง" (Clear), "บันทึก" (Save).
    * แถว 1: น่าจะเป็นสำหรับ "ปิดโปรแกรม" (Quit Program).

### ส่วนที่ 7: เริ่มรันแอป (Part 7: Start the App) ▶️

* Calls the `root.mainloop()` method, which starts the Tkinter event loop. This makes the application window visible and responsive to user interactions.
* **Summary:** This line instructs Tkinter to display the window and wait for user commands.

* เรียกเมธอด `root.mainloop()` ซึ่งเริ่มวงจรเหตุการณ์ของ Tkinter. ทำให้หน้าต่างแอปพลิเคชันปรากฏและตอบสนองต่อการกระทำของผู้ใช้.
* **สรุป:** บรรทัดนี้สั่งให้ Tkinter แสดงหน้าต่างและรอรับคำสั่งจากผู้ใช้.

## วิธีการใช้งาน (How to Use) 🚀

1.  Save the code as a Python file (e.g., `checklist_app.py`).
2.  Ensure you have Python installed with the Tkinter library.
3.  (Optional) Place an icon file named `check.ico` in the same directory as the Python script to use it as the application icon.
4.  Run the script from your terminal or command prompt using `python checklist_app.py`.

1.  บันทึกโค้ดเป็นไฟล์ Python (เช่น `checklist_app.py`).
2.  ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้ง Python พร้อมกับไลบรารี Tkinter แล้ว.
3.  (ไม่บังคับ) วางไฟล์ไอคอนชื่อ `check.ico` ไว้ในไดเรกทอรีเดียวกับสคริปต์ Python หากต้องการใช้เป็นไอคอนของแอปพลิเคชัน.
4.  รันสคริปต์จากเทอร์มินัลหรือพรอมต์คำสั่งโดยใช้ `python checklist_app.py`.

## การปรับปรุงเพิ่มเติม (Further Improvements) ✨

* Implement the actual saving and loading logic for the `saveList()` and `loadList()` functions.
* Complete the `grid()` layout for all widgets to ensure proper arrangement.
* Add labels for the input field and the listbox for better user guidance.
* Consider using a more visually appealing layout and styling (e.g., using `tkinter.ttk`).
* Implement error handling for file operations.

* ปรับปรุงการทำงานของการบันทึกและโหลดข้อมูลในฟังก์ชัน `saveList()` และ `loadList()` ให้สมบูรณ์.
* กำหนดค่า `grid()` layout สำหรับทุก widget ให้สมบูรณ์เพื่อให้การจัดวางถูกต้อง.
* เพิ่มป้ายกำกับ (Label) สำหรับช่องป้อนข้อมูลและกล่องรายการเพื่อให้ผู้ใช้เข้าใจง่ายขึ้น.
* พิจารณาใช้ layout และสไตล์ที่สวยงามยิ่งขึ้น (เช่น ใช้ `tkinter.ttk`).
* เพิ่มการจัดการข้อผิดพลาดสำหรับการดำเนินการเกี่ยวกับไฟล์.

---

<div align="center">
  <img src="anime.gif">
</div>
