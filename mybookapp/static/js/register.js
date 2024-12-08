function validateForm() {
    // Lấy các phần tử input
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirmPassword');
    const passwordError = document.getElementById('passwordError');

    // Kiểm tra mật khẩu và xác nhận mật khẩu
    if (password.value !== confirmPassword.value) {
        // Hiển thị thông báo lỗi nếu mật khẩu không khớp
        passwordError.textContent = 'Mật khẩu và xác nhận mật khẩu không khớp';
        return false;
    } else {
        // Xóa thông báo lỗi nếu mật khẩu khớp
        passwordError.textContent = '';
        return true;
    }
}