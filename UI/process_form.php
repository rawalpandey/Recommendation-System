<?php

$data1 = $_POST["name"];
$data2= $_POST["book"];
$data3= $_POST["song"];
$con=$data1.",".$data2.",".$data3;
$file ="/opt/lampp/htdocs/"."t1.txt";
$handle=fopen($file,'wrx')or die('Unable to open file!'.$file);


fwrite($handle,$con);

fclose($handle);
$message=exec(' python /opt/lampp/htdocs/sample.py 2>&1');
print_r($message);
?>


