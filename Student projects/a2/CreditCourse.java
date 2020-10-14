//Xuan Thanh Le
//Student ID: 500962159
public class CreditCourse extends Course 
{
	private String semester; 
	public double grade; 
	private boolean active; 

	// add a constructor method with appropriate parameters
	// should call the super class constructor
	public CreditCourse(String name, String code, String descr, String fmt, String semester, double grade) 
	{
		super(name, code, descr, fmt); 
		this.semester = semester; 
		this.grade = grade; 
	}

	// get final grade of the student
	public double getGrade() 
	{
		return grade; 
	}

	public boolean getActive() 
	{
		return active; 
	}

	public void setActive() 
	{
		active = true; 
	}

	public void setInactive() 
	{
		active = false; 
	}

	// display numeric Grade
	public String displayGrade() 
	{
		return super.getInfo() + " " + semester + " Grade " + grade + "\n"; 
	}

	// display alphabetic grade
	public String displayAlphabetGrade() 
	{
		return super.getInfo() + " " + semester + " Grade " + super.convertNumericGrade(grade) + "\n"; 
	}

}