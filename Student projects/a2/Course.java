//Xuan Thanh Le
//Student ID: 500962159
public class Course 
{
	public static final double 
	APLUS = 91, A = 85, AMINUS = 80, 
	BPLUS = 77, B = 73, BMINUS = 70, 
	CPLUS = 67, C = 63, CMINUS = 60, 
	DPLUS = 57, D = 53, DMINUS = 50 ; 
	private String code;
	private String name;
	private String description;
	private String format;
	   
	public Course()
	{
	  this.code        = "";
	  this.name        = "";
	  this.description = "";
	  this.format      = "";
	}
	   
	public Course(String name, String code, String descr, String fmt)
	{
	  this.code        = code;
	  this.name        = name;
	  this.description = descr;
	  this.format      = fmt;
	}

	public String getCode()
	{
	   return code;
	}

	public String getName()
	{
	  return name;
	}

	public String getFormat()
	{
	  return format;
	}

	public String getDescription()
	{
	  return code +" - " + name + "\n" + description + "\n" + format;
	}

	 public String getInfo()
	 {
	   return code + " " + name;
	 }

	 
	 // static method to convert numeric score to letter grade string 
	 // e.g. 91 --> "A+"
	 public static String convertNumericGrade(double score)
	 {
		if (score >= APLUS)
	    	return "A+" ;
		else if (score >= A)
			return "A" ;
		else if (score >= AMINUS)
			return "A-" ;
		else if (score >= BPLUS)
			return "B+" ;
		else if (score >= B)
			return "B" ;
		else if (score >= BMINUS)
			return "B-" ;
		else if (score >= CPLUS)
			return "C+" ;
		else if (score >= C)
			return "C" ;
		else if (score >= CMINUS)
			return "C-" ;
		else if (score >= DPLUS)
			return "D+" ;
		else if (score >= D)
			return "D" ;
		else if (score >= DMINUS)
			return "D-" ;
		else 
			return "F" ;
	 }
	 
}
