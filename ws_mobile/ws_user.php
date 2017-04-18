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
	$json_string = json_encode($user, JSON_PRETTY_PRINT);
	print_r($json_string);
	
?>


