
```css
input[type="submit"] {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;  /* Chỉnh lại padding */
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
```

```javascript
// Nhận nút login
var loginButton = document.querySelector('input[type="submit"]');

// Thêm sự kiện click vào nút login
loginButton.addEventListener('click', function() {
    console.log('Login button clicked!');
});
```

```javascript
// Thêm sự kiện mouseover vào nút login
loginButton.addEventListener('mouseover', function() {
    this.style.backgroundColor = '#0056b3';  // Thay đổi màu nền của nút
});

// Thêm sự kiện mouseout để trở lại màu ban đầu khi không rê chuột nữa
loginButton.addEventListener('mouseout', function() {
    this.style.backgroundColor = '#007bff';  // Trở lại màu nền ban đầu
});
```
document.getElementById("loginBtn").addEventListener("click", function () {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Kiểm tra thông tin đăng nhập
    if (username === "admin" && password === "admin") {
        // Chuyển hướng đến trang admin
        window.location.href = "admin/index.html";
    } else {
        // Hiển thị thông báo lỗi
        const errorMessage = document.getElementById("errorMessage");
        errorMessage.classList.remove("hidden");
    }
});