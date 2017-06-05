<?php
    header("Content-Type:text/html; charset=utf-8");
    $Temperature=$_POST[Temp];
    $Humidity=$_POST[Humi];
    $SensorID=$_POST[sensor];

    if ($SensorID == 1) {
        $fp = fopen('/home/pi/www-data/temp.txt', 'w');
        fwrite($fp, $Temperature);
        fwrite($fp, $Humidity);
        fclose($fp);
    }
?>
