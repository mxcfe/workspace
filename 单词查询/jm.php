<?php

$str1= str_replace(" ","%20",$_GET['word']);

// $url='https://dict.youdao.com/suggest?doctype=json&le=eng&num=15&q='.$str1.'&ver=3';
$url='https://dict.youdao.com/suggest?num=5&doctype=json&cache=false&le=en&q='.$str1.'&ver=3.0';

$html= file_get_contents($url);
$web = json_decode($html);
// echo ($web->data->entries[0]->explain);
// if (!strcasecmp($web->data->entries[0]->entry,$_GET['word'])){
//  echo ($web->data->entries[0]->explain);}

?>