<!doctype html>
<html lang='en'>

<head>
	<meta charset="UTF-8">
	<title>Rosenburg WebApp - BMI Calculator</title>
	<style>
        .error {
          color: #FF0000;
        }
    </style>
</head>

<body>
<h1><b>BMI Calculator</b></h1>
<p><span>Please enter the following information.</span></p>

	<?php
		function sanitizeString($var)
		{
			$var = stripslashes($var);
			$var = strip_tags($var);
			$var = htmlentities($var);
			$var = trim($var);
			return $var;
		}
		
		//initialize variables
		$weight = "";
		$weightErr = "";
		
		$feet = "";
		$feetErr = "";
		
		$inches = "";
		$inchesErr = "";
		
		$bmiAnswer = "????";
		$categoryAnswer = "????";
		
		if (isset($_POST['Submit']))
		{
			$noErr = true;
			
			//validate weight value
			$temp = sanitizeString($_POST['weight']);
			if ((filter_var($temp, FILTER_VALIDATE_INT) === false) or ($temp < 0))
			{
				$noErr = false;
				$weightErr = "Must be a non-negative integer";
				$weight = "";
			}
			else
			{
				$weight = $temp;
				$weightErr = "";
			}
			
			//validate feet value
			$temp = sanitizeString($_POST['feet']);
			if ((filter_var($temp, FILTER_VALIDATE_INT) === false) or ($temp < 0))
			{
				$noErr = false;
				$feetErr = "Must be a non-negative integer";
				$feet = "";
			}
			else
			{
				$feet = $temp;
				$feetErr = "";
			}
			
			//validate inches value
			$temp = sanitizeString($_POST['inches']);
			if ((filter_var($temp, FILTER_VALIDATE_INT) === false) or ($temp < 0))
			{
				$noErr = false;
				$inchesErr = "Must be a non-negative integer";
				$inches = "";
			}
			else
			{
				$inches = $temp;
				$inchesErr = "";
			}
			
			//Run calculation if all inputs are valid.
			if ($noErr == false)
			{
				$bmiAnswer = "????";
				$categoryAnswer = "????";
			}
			else
			{
				$totalInches = $inches + ($feet * 12);
				$bmiAnswer = round((703 * $weight) / pow($totalInches, 2), 1);
				
				if ($bmiAnswer < 18.5) $categoryAnswer = "Underweight";
				else if ($bmiAnswer < 25) $categoryAnswer = "Normal Weight";
				else if ($bmiAnswer < 30) $categoryAnswer = "Overweight";
				else $categoryAnswer = "Obese";
			}
		}
	?>

	<form method="post" action="bmiCalculator.php">
	
		Weight(in pounds): <input type="text" size="3" name="weight" value="<?php echo $weight ?>">
		<span class="error"><?php echo $weightErr ?></span>
		<br><br>
		
		Height(feet): <input type="text" size="3" name="feet" value="<?php echo $feet ?>">
		<span class="error"><?php echo $feetErr ?></span>
		<br><br>
		
		Height(inches): <input type="text" size="3" name="inches" value="<?php echo $inches ?>">
		<span class="error"><?php echo $inchesErr ?></span>
		<br><br>
		
		<input type="submit" name="Submit" value="Calculate">
		<br><br>
		
	</form>
	
<p>Your current BMI is <b><?php echo $bmiAnswer ?></b>, Category:<b><?php echo $categoryAnswer ?></b><p>
<br>
<br>

<a href="Rosenburg.php"><b>Home Page</b></a>
</body>

</html>
