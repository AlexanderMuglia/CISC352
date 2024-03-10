(define (problem p3-dungeon)
  (:domain Dungeon)

  ; Naming convention:
  ; - loc-{i}-{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc-{i}-{j} and loc-{h}-{k}
  (:objects
    loc-3-4 loc-4-5 loc-1-2 loc-2-2 loc-3-2 loc-3-3 loc-2-5 loc-1-3 loc-2-1 loc-1-4 loc-3-5 loc-2-4 loc-4-4 loc-2-3 loc-4-3 - location
    c2122 c1222 c2232 c1213 c1223 c2223 c3223 c3233 c1323 c2333 c1314 c2314 c2324 c2334 c3334 c1424 c2434 c2425 c2535 c3545 c4544 c4443 - corridor
    key1 key2 key3 key4 key5 key6 - key
  )

  (:init

    ; Hero location and carrying status
    (hero-at loc-2-1)
    (free-hand)

    ; Locationg <> Corridor Connections
    (corridor-to c2122 loc-2-1)
    (corridor-to c2122 loc-2-2)

    (corridor-to c1222 loc-1-2)
    (corridor-to c1222 loc-2-2)

    (corridor-to c2232 loc-2-2)
    (corridor-to c2232 loc-3-2)

    (corridor-to c1213 loc-1-2)
    (corridor-to c1213 loc-1-3)

    (corridor-to c1223 loc-1-2)
    (corridor-to c1223 loc-2-3)

    (corridor-to c2223 loc-2-2)
    (corridor-to c2223 loc-2-3)

    (corridor-to c3223 loc-3-2)
    (corridor-to c3223 loc-2-3)

    (corridor-to c3233 loc-3-2)
    (corridor-to c3233 loc-3-3)

    (corridor-to c1323 loc-1-3)
    (corridor-to c1323 loc-2-3)

    (corridor-to c2333 loc-2-3)
    (corridor-to c2333 loc-3-3)

    (corridor-to c1314 loc-1-3)
    (corridor-to c1314 loc-1-4)

    (corridor-to c2314 loc-2-3)
    (corridor-to c2314 loc-1-4)

    (corridor-to c2324 loc-2-3)
    (corridor-to c2324 loc-2-4)

    (corridor-to c2334 loc-2-3)
    (corridor-to c2334 loc-3-4)

    (corridor-to c3334 loc-3-3)
    (corridor-to c3334 loc-3-4)

    (corridor-to c1424 loc-1-4)
    (corridor-to c1424 loc-2-4)

    (corridor-to c2434 loc-2-4)
    (corridor-to c2434 loc-3-4)

    (corridor-to c2425 loc-2-4)
    (corridor-to c2425 loc-2-5)

    (corridor-to c2535 loc-2-5)
    (corridor-to c2535 loc-3-5)

    (corridor-to c3545 loc-3-5)
    (corridor-to c3545 loc-4-5)

    (corridor-to c4544 loc-4-5)
    (corridor-to c4544 loc-4-4)

    (corridor-to c4443 loc-4-4)
    (corridor-to c4443 loc-4-3)
    
    ; Key locations
    (key-here key1 loc-2-1)
    (key-here key2 loc-2-3)
    (key-here key3 loc-2-3)
    (key-here key4 loc-2-3)
    (key-here key5 loc-2-3)
    (key-here key6 loc-4-4)
    
    ; Locked corridors
    (locked c1223)
    (locked-with c1223 red)
    
    (locked c2223)
    (locked-with c2223 red)
    
    (locked c3223)
    (locked-with c3223 red)
    
    (locked c1323)
    (locked-with c1323 red)
    
    (locked c2333)
    (locked-with c2333 red)
    
    (locked c2314)
    (locked-with c2314 red)
    
    (locked c2324)
    (locked-with c2324 red)
    
    (locked c2334)
    (locked-with c2334 red)
    
    (locked c2425)
    (locked-with c2425 purple)
    
    (locked c2535)
    (locked-with c2535 green)
    
    (locked c3545)
    (locked-with c3545 purple)
    
    (locked c4544)
    (locked-with c4544 green)
    
    (locked c4443)
    (locked-with c4443 rainbow)

    ; Risky corridors
    (risky c1223)
    (risky c2223)
    (risky c3223)
    (risky c1323)
    (risky c2333)
    (risky c2314)
    (risky c2324)
    (risky c2334)
    
    ; Key colours
    (key-colour key1 red)
    (key-colour key2 green)
    (key-colour key3 purple)
    (key-colour key4 green)
    (key-colour key5 purple)
    (key-colour key6 rainbow)
    
    ; Key usage properties (one use, two use, etc)
    (multi-use key1)
    (one-use key2)
    (one-use key3)
    (one-use key4)
    (one-use key5)
    (one-use key6)
    
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
      (hero-at loc-4-3)
    )
  )

)
