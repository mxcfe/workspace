<?php

$url='https://dict.youdao.com/jsonapi_s?client=mobile&le=eng&q='.$_GET['word'].'&dicts=%7B%22count%22%3A1%2C%22dicts%22%3A%5B%5B%22individual%22%5D%5D%7D&client=mobile&keyfrom=mdict.9.1.6.iphonepro&imei=5be7807386c8b610f9aa1ee6e55e23f8&model=iPad&deviceid=5be7807386c8b610f9aa1ee6e55e23f8&mid=15.1&username=&vendor=AppStore&userid=&device=iPad11,3&idfa=00000000-0000-0000-0000-000000000000&guestNonce=3170738076197216278&abtest=3&network=wifi&guestSig=57E2538669A6355CD08CE8AF995DE9A8&appVersion=9.1.6&previewEnvTest=0&jsonversion=4&source=main&t=1636442092915&sign=01d6bf64cb7a104b8c3a17680e8c8d0a&userLabel=LEARNER,HIGHSCHOOL,GRADUATEEXAM';

$html= file_get_contents($url);
$web = json_decode($html);
alert($web)

$arr = $web->individual->trs;


$s='{';
foreach ($arr as $value) {
	$s=$s.'"'.$value->pos.'":"'.$value->tran.'",';

	
}
$s=$s.'}';
echo json_encode($web->individual);

?>