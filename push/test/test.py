from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Khởi tạo WebDriver (mở trình duyệt Chrome)
driver = webdriver.Chrome()

# Mở trang web cần kiểm tra
# https://nguyenquocloc2003.github.io/project/push/test/index.html
driver.get("https://rough-earthy-cotton.glitch.me/")

# Hàm kiểm tra kết quả từng test case
def check_result(driver, num1, num2, expected_result):
    # Nhập giá trị vào ô "Số thứ 1"
    driver.find_element(By.ID, "num1").clear()
    driver.find_element(By.ID, "num1").send_keys(str(num1))
    
    # Nhập giá trị vào ô "Số thứ 2"
    driver.find_element(By.ID, "num2").clear()
    driver.find_element(By.ID, "num2").send_keys(str(num2))
    
    # Nhập giá trị kỳ vọng vào ô "Kết quả"
    driver.find_element(By.ID, "num3").clear()
    driver.find_element(By.ID, "num3").send_keys(str(expected_result))

    # Nhấn nút "Kiểm tra"
    driver.find_element(By.XPATH, "//button[text()='Kiểm tra']").click()

    # Chờ thông báo hiển thị (div có id="notification")
    try:
        notification = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "notification"))
        )
        print(f"\033[33mThông báo hiển thị:\033[0m {notification.text}")  # Nội dung thông báo
    except Exception as e:
        print(f"\033[31mKhông có thông báo hiển thị sau 10 giây. Lỗi:\033[0m {e}")
    
    # Thêm dòng phân cách (====================)
    print(f"\033[35m{'=' * 100}\033[0m")  # Màu tím cho dòng phân cách

    # Chờ thêm 1 giây để đảm bảo tất cả trạng thái hoàn tất
    time.sleep(1)

# Danh sách các test case
test_cases = [
    (5, 3, 8),       # Đúng
    (7, 4, 12),      # Sai
    (1, 1, 2),       # Đúng
    (3, 5, 8),       # Đúng
    (12, 7, 19),     # Đúng
    (8, 2, 10),      # Đúng
    (15, 9, 24),     # Đúng
    (4, 5, 8),       # Sai
    (9, 5, 14),      # Đúng
    (5, 3, 9),       # Sai
    (10, 7, 17),     # Đúng
    (6, 7, 13),      # Sai
    (13, 8, 21),     # Đúng
    (6, 8, 14),      # Sai
    (13, 5, 17),     # Sai
    (20, 5, 25),     # Đúng
    (10, 10, 19),    # Sai
    (17, 5, 22),     # Sai
    (11, 3, 15),     # Đúng
    (0, 0, 0),       # Đúng
    (14, 9, 23),     # Đúng
    (4, 6, 10),      # Đúng
    (9, 7, 17),      # Sai
    (18, 4, 22),     # Đúng
    (10, 5, 15),     # Đúng
    (8, 9, 16),      # Sai
    (7, 3, 10),      # Sai
]

# Chạy qua từng test case
for num1, num2, expected_result in test_cases:
    print(f"\033[36mKiểm tra với {num1} + {num2} = {expected_result}\033[0m")
    check_result(driver, num1, num2, expected_result)

# Đóng trình duyệt sau khi hoàn tất
driver.quit()
