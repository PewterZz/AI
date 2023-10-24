% Define a predicate to check if the sum of two angles is 90 degrees
is_right_triangle(Angle1, Angle2) :-
    Sum is Angle1 + Angle2,
    Sum =:= 90.

% Define a predicate to check if a given triangle is a right triangle
right_triangle(Angle1, Angle2, Angle3) :-
    ( is_right_triangle(Angle1, Angle2);
      is_right_triangle(Angle1, Angle3);
      is_right_triangle(Angle2, Angle3) ),
    Total is Angle1 + Angle2 + Angle3,
    Total =:= 180.
