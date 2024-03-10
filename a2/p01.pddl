(define (problem p1-dungeon)
  (:domain Dungeon)

  ; Naming convention:
  ; - loc-{i}-{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc-{i}-{j} and loc-{h}-{k}
  (:objects
    loc-3-1 loc-1-2 loc-2-2 loc-3-2 loc-4-2 loc-2-3 loc-3-3 loc-2-4 loc-3-4 loc-4-4 - location
    key1 key2 key3 key4 - key
    c3132 c1222 c2232 c3242 c2223 c3233 c2333 c2324 c3334 c2434 c3444 - corridor
  )

  (:init

    ; Hero location and carrying status
    (hero-at loc-1-2)
    (free-hand)
    ; Locationg <> Corridor Connections
    (corridor-to c3132 loc-3-1)
    (corridor-to c3132 loc-3-2)
        
    (corridor-to c1222 loc-1-2)
    (corridor-to c1222 loc-2-2)
    
    (corridor-to c2232 loc-2-2)
    (corridor-to c2232 loc-3-2)
    
    (corridor-to c3242 loc-3-2)
    (corridor-to c3242 loc-4-2)
    
    (corridor-to c2223 loc-2-2)
    (corridor-to c2223 loc-2-3)
    
    (corridor-to c3233 loc-3-2)
    (corridor-to c3233 loc-3-3)
    
    (corridor-to c2333 loc-2-3)
    (corridor-to c2333 loc-3-3)
    
    (corridor-to c2324 loc-2-3)
    (corridor-to c2324 loc-2-4)
    
    (corridor-to c3334 loc-3-3)
    (corridor-to c3334 loc-3-4)
    
    (corridor-to c2434 loc-2-4)
    (corridor-to c2434 loc-3-4)
    
    (corridor-to c3444 loc-3-4)
    (corridor-to c3444 loc-4-4)

    ; Key locations
    (key-here key1 loc-2-2)
    (key-here key2 loc-4-2)
    (key-here key3 loc-2-4)
    (key-here key4 loc-4-4)

    ; Locked corridors
    (locked c3132)
    (locked-with c3132 rainbow)
    
    (locked c3242)
    (locked-with c3242 purple)
    
    (locked c2324)
    (locked-with c2324 red)
    
    (locked c2434)
    (locked-with c2434 red)
    
    (locked c3444)
    (locked-with c3444 yellow)
    
    ; Risky corridors
    (risky c2324)
    (risky c2434)
    
    ; Key colours
    (key-colour key1 red)
    (key-colour key2 rainbow)
    (key-colour key3 yellow)
    (key-colour key4 purple)

    ; Key usage properties (one use, two use, etc)
    (multi-use key1)
    (one-use key2)
    (two-use key3)
    (one-use key4)
    
    (has-uses key1)
    (has-uses key2)
    (has-uses key3)
    (has-uses key4)
    
  )
  (:goal
    (and
      ; Hero's final location goes here
      (hero-at loc-3-1)
    )
  )

)
