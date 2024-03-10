(define (problem p4-dungeon)
  (:domain Dungeon)

  ; Come up with your own problem instance (see assignment for details)
  ; NOTE: You _may_ use new objects for this problem only.

  ; Naming convention:
  ; - loc-{i}-{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc-{i}-{j} and loc-{h}-{k}
  (:objects
    loc-1-1 loc-1-2 loc-1-3 loc-2-1 loc-2-2 loc-2-3 loc-3-1 loc-3-2 loc-3-3 - location
    c1112 c1213 c1323 c2333 c3332 c3231 c3121 c2122 c1121 - corridor
    key1 key2 key3 key4 key5 key6 - key
  )

  (:init

    ; Hero location and carrying status
    (hero-at loc-2-3)
    (free-hand)

    ; Locationg <> Corridor Connections
    (corridor-to c1112 loc-1-1)
    (corridor-to c1112 loc-1-2)

    (corridor-to c1213 loc-1-2)
    (corridor-to c1213 loc-1-3)

    (corridor-to c1323 loc-1-3)
    (corridor-to c1323 loc-2-3)

    (corridor-to c2333 loc-2-3)
    (corridor-to c2333 loc-3-3)

    (corridor-to c3332 loc-3-3)
    (corridor-to c3332 loc-3-2)

    (corridor-to c3231 loc-3-2)
    (corridor-to c3231 loc-3-1)

    (corridor-to c3121 loc-3-1)
    (corridor-to c3121 loc-2-1)

    (corridor-to c2122 loc-2-1)
    (corridor-to c2122 loc-2-2)
    
    (corridor-to c1121 loc-1-1)
    (corridor-to c1121 loc-2-1)

    ; Key locations
    (key-here key1 loc-1-1)
    (key-here key2 loc-1-1)
    (key-here key3 loc-1-1)
    (key-here key4 loc-1-1)
    (key-here key5 loc-1-1)
    (key-here key6 loc-2-1)

    
    ; Locked corridors
    (locked c2333)
    (locked-with c2333 green)
    
    (locked c3332)
    (locked-with c3332 purple)
    
    (locked c3231)
    (locked-with c3231 yellow)
    
    (locked c3121)
    (locked-with c3121 purple)
    
    (locked c2122)
    (locked-with c2122 rainbow)
    
    (locked c1121)
    (locked-with c1121 red)
    
    ; Risky corridors
    (risky c1121)  
    
    ; Key colours
    (key-colour key1 rainbow)
    (key-colour key2 green)
    (key-colour key3 purple)
    (key-colour key4 yellow)
    (key-colour key5 purple)
    (key-colour key6 red)
    
    ; Key usage properties (one use, two use, etc)
    (one-use key1)
    (one-use key2)
    (one-use key3)
    (two-use key4)
    (one-use key5)
    (multi-use key6)

    (has-uses key1)
    (has-uses key2)
    (has-uses key3)
    (has-uses key4)
    (has-uses key5)
    (has-uses key6)

  )
  (:goal
    (and
      ; Hero's final location goes here
      (hero-at loc-2-2)
    )
  )

)
