(define (problem p2-dungeon)
  (:domain Dungeon)
;
  ; Naming convention:
  ; - loc-{i}-{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc-{i}-{j} and loc-{h}-{k}
  (:objects
    loc-2-1 loc-1-2 loc-2-2 loc-3-2 loc-4-2 loc-2-3 - location
    key1 key2 key3 key4 - key
    c2122 c1222 c2232 c3242 c2223 - corridor
  )

  (:init

    ; Hero location and carrying status
    (hero-at loc-2-2)
    (free-hand)
    ; Locationg <> Corridor Connections
    (corridor-to c2122 loc-2-1)
    (corridor-to c2122 loc-2-2)
        
    (corridor-to c1222 loc-1-2)
    (corridor-to c1222 loc-2-2)
    
    (corridor-to c2232 loc-2-2)
    (corridor-to c2232 loc-3-2)
    
    (corridor-to c3242 loc-3-2)
    (corridor-to c3242 loc-4-2)
    
    (corridor-to c2223 loc-2-2)
    (corridor-to c2223 loc-2-3)

    ; Key locations
    (key-here key1 loc-2-1)
    (key-here key2 loc-1-2)
    (key-here key3 loc-2-2)
    (key-here key4 loc-2-3)
    
    ; Locked corridors
    (locked c2122)
    (locked-with c2122 purple)
    
    (locked c1222)
    (locked-with c1222 yellow)
    
    (locked c2232)
    (locked-with c2232 yellow)
    
    (locked c3242)
    (locked-with c3242 rainbow)
    
    (locked c2223)
    (locked-with c2223 green)
    
    ; Risky corridors

    ; Key colours
    (key-colour key1 green)
    (key-colour key2 rainbow)
    (key-colour key3 purple)
    (key-colour key4 yellow)
    
    ; Key usage properties (one use, two use, etc)
    (one-use key1)
    (one-use key2)
    (one-use key3)
    (two-use key4)
    
    (has-uses key1)
    (has-uses key2)
    (has-uses key3)
    (has-uses key4)
  )
  (:goal
    (and
      ; Hero's final location goes here
      (hero-at loc-4-2)
    )
  )

)
