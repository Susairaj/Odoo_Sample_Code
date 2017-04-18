<?php
	$url = "http://demo.cristolive.org:9069";
	$db = "cristo_ind_demo";
	$username = "ylgpo.2016@gmail.com";
	$password = "cristo@2016";
	
	//lib
	require_once('ripcord.php');
	
	$common = ripcord::client("$url/xmlrpc/2/common");
	//print_r($common->version());
	
	//authenticate
	$uid = $common->authenticate($db, $username, $password, array());
	echo $uid;
	
	//xmlrpc object
	$models = ripcord::client("$url/xmlrpc/2/object");
	
	//search read
	$user = $models->execute_kw($db, $uid, $password,
		'res.users', 'search_read',
		array(array(array('id', '=',$uid))),
		array('fields'=>array('diocese_id','vicariate_id','parish_id', 'name')));
		
	echo "<pre>";
	$json_str_user = json_encode($user, JSON_PRETTY_PRINT);
	echo "<br />User<br />";
	print_r($json_str_user);

	if($user){
		$parish = $models->execute_kw($db, $uid, $password,
			'res.parish', 'search_read',
			array(array(array('id', '=',$user[0]['parish_id'][0]))),
			array('fields'=>array('name','image','history')));
		$json_str_parish = json_encode($parish, JSON_PRETTY_PRINT);
		echo "<br />Parish<br />";
		print_r($json_str_parish);
	}
	
?>


