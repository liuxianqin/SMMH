<?php
$handler=opendir('.');

while(($filename=readdir($handler))!==false)
{
	if($filename!="."&& $filename!="..")
	{
		echo $filename."<br>";
	}
}

