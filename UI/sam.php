<!doctype>
<html>
<head>
<title> data insertion and fetch </title>
 <style type="text/css">
 	.in
			{
			color:white;
			position:relative;
			left:110px;
			top:5px;
			font:normal 20px/2.0em Sans-Serif;
			}
		 p{
			text-align:center;
			color:white;
			font-size:16.8px;
			}
	
			#topbar
			{
			margin:auto;
			width:1900px;
			height:1500px;
			background-image:url('back.jpg');
			
			
			}
			#title
			{
					 position:relative;
						top:200px;

						left:550px;
			}
			#ti
			{
				color:white;
				font:normal 60px/2.0em Sans-Serif;
			
			}
			#uni1
			{
				background-image:url('m1.jpg');
			}
			#uni2
			{	

				background-image:url('novel.jpg');		
			}
			#uni3
			{
				background-image:url('song.jpg');	
			}
			.first
			{
			width:600px;
			
			height:500px;
			float:left;
			margin:15px;
			position:relative;
			top:200px;
			}
			.set{
			width:80px;
			height:80px;
			position:relative;
			left:100px;
			top:20px;
			}
			.first:hover{opacity:0.1; color:white;}
					#abc{
		text-align:center;
		
		font-family: sans-serif;
		font-size: 100px;
		color:white;
		width:200px;
		height:100px;
		position: relative;
		left:150px;
		top:100px;
		

		}
		#ip
		{
			position: relative;
		left:100px;
		top:400px;
		}
		#pos
		{
			position:relative;
			top:200px;
			left:700px;
		}
        


 </style>
</head>
<body>
<div id="topbar">
	<div id="title">
			<h1 id="ti"><b>Recommendation System</h1>


	</div>
   



   <div class="first" id="uni1"><h1 id="abc">Movies</h1>
			
			</div>
			<div class="first" id="uni2"><h1 id="abc">Books</h1>

			
			</div>
			<div class="first" id="uni3" ><h1 id="abc">Songs</h1>
			
			</div>
		<body>
<div id="ip">	
<form action="process_form.php" method="POST">
        <div style="padding-left:30px;">
            <div style="float:left;" >
                <input type="text" name="name" id="" placeholder="Enter recently watched movie" class="input" size="35">
            </div>
            <div style="float:left;padding-left:430px;" >
                <input type="text" name="book" id="" placeholder="Enter recently read book" class="input" size="35">
            </div>
            <div style="float:left;padding-left:430px;" >
                <input type="text" name="song" id="" placeholder="Enter recently played song" class="input" size="35">
            </div>
            <div style="padding-left:70px" >
                <input id="pos" type="submit" name="submit">
            </div>

        </div>
</body>


</div>
</body>
</html>
