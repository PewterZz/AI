is_right_triangle(Angle1, Angle2) :-
    Sum is Angle1 + Angle2,
    Sum =:= 90.

right_triangle(Angle1, Angle2, Angle3) :-
    ( is_right_triangle(Angle1, Angle2);
      is_right_triangle(Angle1, Angle3);
      is_right_triangle(Angle2, Angle3) ),
    Total is Angle1 + Angle2 + Angle3,
    Total =:= 180.
