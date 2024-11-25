<?php
if (isset($_GET['integers']) && isset($_GET['threshold'])) {
    $integers = $_GET['integers'];
    $threshold = $_GET['threshold'];

    $command = escapeshellcmd("python3 bitwise_operations.py '$integers' $threshold");
    $output = shell_exec($command);

    echo "<h2>Results:</h2>";
    echo $output;
} else {
    echo "<h2>Error:</h2>";
    echo "<p>Missing required parameters.</p>";
}
?>