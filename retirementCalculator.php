<!doctype html>
<html lang='en'>

<head>
	<meta charset="UTF-8">
	<title>Rosenburg WebApp - Retirement</title>
	<style>
        .error {
          color: #FF0000;
        }
    </style>
</head>

<body>
<h1><b>Retirement Age Calculator</b></h1>
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
		
		//initialize variables to be nothing
		$salary = "";
		$salaryErr = "";
		
		$percent = "";
		$percentErr = "";
		
		$currentAge = "";
		$currentAgeErr = "";
		
		$goal = "";
		$goalErr = "";
		
		$ageAnswer = "????";
		
		//run if user presses submit button
		if (isset($_POST['Submit']))
		{
			$noErr = true;
			
			//validate salary value
			$temp = sanitizeString($_POST['salary']);
			if ((filter_var($temp, FILTER_VALIDATE_FLOAT) === false) or ($temp < 0))
			{
				$salary = "";
				$salaryErr = "Enter a non-negative numeral";
				$noErr = false;
			}
			else
			{
				$salary = $temp;
				$salaryErr = "";
			}
			
			//validate percent value
			$temp = sanitizeString($_POST['percent']);
			if ((filter_var($temp, FILTER_VALIDATE_FLOAT) === false) or ($temp < 0) or ($temp > 100))
			{
				$percent = "";
				$percentErr = "Enter a number between 1 and 100";
				$noErr = false;
			}
			else
			{
				$percent = $temp;
				$percentErr = "";
			}
			
			//validate currentAge value
			$temp = sanitizeString($_POST['currentAge']);
			if ((filter_var($temp, FILTER_VALIDATE_INT) === false) or ($temp < 1) or ($temp > 99))
			{
				$currentAge = "";
				$currentAgeErr = "Enter a number between 1 and 99";
				$noErr = false;
			}
			else
			{
				$currentAge = $temp;
				$currentAgeErr = "";
			}
			
			//validate goal value
			$temp = sanitizeString($_POST['goal']);
			if ((filter_var($temp, FILTER_VALIDATE_FLOAT) === false) or ($temp < 1))
			{
				$goal = "";
				$goalErr = "Enter a non-negative numeral";
				$noErr = false;
			}
			else
			{
				$goal = $temp;
				$goalErr = "";
			}
			
			//Run calculation if all inputs are valid
			
			if ($noErr == false)
			{
				$ageAnswer = "????";
			}
			else
			{
				$percentofSalary = $percent / 100;
				$yearlySavings = $salary * $percentofSalary * 1.35;
				$years = round($goal / $yearlySavings);
				$goalAge = $years + $currentAge;
				
				if ($goalAge > 100)
				{
					$ageAnswer = "<span class='error'>Your goal is not possible in your lifetime.</span>";
				}
				else $ageAnswer = $goalAge;
			}
		}
	?>

	<form method="post" action="retirementCalculator.php">
	
		Yearly Salary: $<input type="text" size="20" name="salary" value="<?php echo $salary ?>">
		<span class="error"><?php echo $salaryErr ?></span>
		<br><br>
		
		Percent of Salary Saved: <input type="text" size="3" name="percent" value="<?php echo $percent ?>">%
		<span class="error"><?php echo $percentErr ?></span>
		<br><br>
		
		Your Current Age: <input type="text" size="3" name="currentAge" value="<?php echo $currentAge ?>">
		<span class="error"><?php echo $currentAgeErr ?></span>
		<br><br>
		
		How much do you plan to save for retirement?: $<input type="text" size="20" name="goal" value="<?php echo $goal ?>">
		<span class="error"><?php echo $goalErr ?></span>
		<br><br>
		
		<input type="submit" name="Submit" value="Calculate">
		<br><br>
		
	</form>

<p>At your current rate, you will be able to retire at the age of: <b><?php echo $ageAnswer ?></b></p>
<br>
<br>

<a href="Rosenburg.php"><b>Home Page</b></a>
</body>

</html>