<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kết Quả Tính Toán</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
            text-align: center;
            padding: 20px;
        }
        h1 {
            color: #ff6347; /* Màu đỏ */
            font-size: 2.5em;
        }
        h2 {
            color: #4682b4; /* Màu xanh biển */
        }
        .result {
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 20px;
            margin: 20px auto;
            max-width: 600px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>

<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $num1 = isset($_POST['num1']) ? $_POST['num1'] : '';
    $num3 = isset($_POST['num3']) ? $_POST['num3'] : '';
    $num4 = $num1 * $num3;

    echo "<div class='result'>";

    for ($a = 1; $a <= 1; $a++) {
        if ($num4 == 10) {
            echo $num4 . " là kết quả";
            for ($c = 1; $c <= 100; $c++) {
                echo "<h2>$c Anh yêu em</h2>";
            }
            break;
        }
        if ($num4 == 20) {
            header('Location: traitim.html');
            exit();
        }
        if ($num4 <= 100) {
            echo "$num4 dưới 100<br>";
            echo "<h1>Anh Lộc Đẹp Trai Vãi Lồn</h1>";
        } else {
            echo "$num4 trên 100<br>";
        }
    }

    echo "</div>";
} else {
    echo "<div class='result'>Không có dữ liệu gửi đến</div>";
}
?>

</body>
</html>

