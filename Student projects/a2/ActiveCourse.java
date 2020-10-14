//Xuan Thanh Le
//Student ID: 500962159

import com.sun.source.tree.Tree;

import java.util.ArrayList;
import java.util.Collections; 
import java.util.Comparator;
import java.util.TreeMap;

// Active University Course

public class ActiveCourse extends Course 
{
   private ArrayList < Student > students; 
   private String semester;
   private TreeMap<String, ArrayList<int[]>> lectureInfo;

   // Add a constructor method with appropriate parameters
   // should call super class constructor to initialize inherited variables
   // make sure to *copy* students array list being passed in into new arraylist of
   // students
   // see class Registry to see how an ActiveCourse object is created and used
   public ActiveCourse(String name, String code, String descr, String fmt, String semester, 
         ArrayList < Student > students) 
   {
      super(name, code, descr, fmt); 
      this.semester = semester; 
      ArrayList < Student > st = new ArrayList<>();
      st.addAll(students);
      this.students = st;
      lectureInfo = new TreeMap<>();
      lectureInfo.put("Mon", new ArrayList<>());
      lectureInfo.put("Tue", new ArrayList<>());
      lectureInfo.put("Wed", new ArrayList<>());
      lectureInfo.put("Thu", new ArrayList<>());
      lectureInfo.put("Fri", new ArrayList<>());

   }

   // add new students to classList;
   public void addStudents(Student st) 
   {
      for (Student s:students) 
      {
         if (s.equals(st)) 
         {
            return; 
         }
      }
      students.add(st); 
   }


   public void setLectureInfo(int ls, int ld, String day) {
      int[] block = {ls, ls + ld*100};
      lectureInfo.get(day).add(block);
   }
   public TreeMap<String, ArrayList<int[]>> getLectureInfo() {
      return lectureInfo;
   }
   // return the class list
   public ArrayList < Student > getStudents() 
   {
      return students; 
   }

   // remove students from class list
   public void removeStudent(String studentId) 
   {
      int index = 0; 
      boolean found = false; 
      for (Student st:students) 
      {
         if (studentId.equalsIgnoreCase(st.getId())) 
         {
            index = students.indexOf(st); 
            found = true; 
         }
      }
      if (found) 
      {
         students.remove(index); 

      }
   }

   // get semester;
   public String getSemester() 
   {
      return semester; 
   }

   // Prints the students in this course (name and student id)
   public void printClassList() 
   {
      for (Student st:students) 
      {
         System.out.println(st + " " + st.getId()); 
      }
   }

   // Prints the grade of each student in this course (along with name and student
   // id)
   public void printGrades() 
   {
      for (Student st:students) 
      {
         System.out.println(st.getName() + " " + st.getId() + " " + getGrade(st.getId())); 
      }
   }

   // Returns the numeric grade in this course for this student
   // If student not found in course, return 0
   public double getGrade(String studentId) 
   {
      for (Student st:students) 
      {
         if (st.getId().equals(studentId))
         {
            return st.getStudentGrade(); 
         }
      }
      // Search the student's list of credit courses to find the course code that
      // matches this active course
      // see class Student method getGrade()
      // return the grade stored in the credit course object
      return 0;
   }

   // Returns a String containing the course information as well as the semester
   // and the number of students
   // enrolled in the course
   // must override method in the superclass Course and use super class method
   // getDescription()
   public String getCourseDescription() 
   
   {
      return super.getDescription() + "\n" + semester + "\n" + "Enrolment " + students.size() + "\n";
   }

   // Sort the students in the course by name using the Collections.sort() method
   // with appropriate arguments
   // Make use of a private Comparator class below
   public void sortByName() 
   
   {
      Collections.sort(students, new NameComparator());
   }

   // Fill in the class so that this class implement the Comparator interface
   // This class is used to compare two Student objects based on student name
   private class NameComparator implements Comparator<Student> 
   
   {
      public int compare(Student s1, Student s2) 
      
      {
         return s1.getName().compareTo(s2.getName());
      }
   }

   // Sort the students in the course by student id using the Collections.sort()
   // method with appropriate arguments
   // Make use of a private Comparator class below
   public void sortById() 
   
   {
      Collections.sort(students, new IdComparator());
   }

   // Fill in the class so that this class implement the Comparator interface
   // This class is used to compare two Student objects based on student id
   private class IdComparator implements Comparator<Student> 

   {
      public int compare(Student s1, Student s2) 
      
      {
         return s1.getId().compareTo(s2.getId());
      }
   }
}
