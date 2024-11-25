<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>assigment 6 bitwise_operations form</title>
</head>
<body>
    <h2>Enter Integers for Bitwise Operations</h2>
    <form action="process.php" method="GET">
        <label for="integers">Enter integers separated by commas:</label><br>
        <input type="text" id="integers" name="integers" required><br><br>
        
        <label for="threshold">Enter threshold:</label><br>
        <input type="number" id="threshold" name="threshold" required><br><br>
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>