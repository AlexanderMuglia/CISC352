(define (domain Dungeon)

    (:requirements
        :typing
        :negative-preconditions
        :conditional-effects
    )

    ; Do not modify the types
    (:types
        location colour key corridor
    )

    ; Do not modify the constants
    (:constants
        red yellow green purple rainbow - colour
    )

    ; You may introduce whatever predicates you would like to use
    (:predicates

        ; One predicate given for free!
        (hero-at ?loc - location)

        ; There is a locked door in ?cor
        (locked ?cor - corridor)
        ; Corridor is risky 
        (risky ?cor - corridor)
        ; Corridor has collapsed 
        (collapsed ?cor - corridor)
        ; Room is messy 
        (messy ?loc - location)
        ; There is a key ?k at ?loc
        (key-here ?k - key ?loc - location)
        ; The hero has a free hand
        (free-hand)
        ; The hero is holding key ?k
        (holding ?k - key)
        ; The key ?k has some uses left
        (has-uses ?k - key)
        ; Corridor ?cor is locked with colour ?col 
        (locked-with ?cor - corridor ?col - colour)
        ; Key ?k is is colour ?col 
        (key-colour ?k - key ?col - colour)
        ; Corridor ?cor leads to location ?loc
        (corridor-to ?cor - corridor ?loc - location)
        ; Key ?k is two-use
        (two-use ?k - key)
        ; Key ?k is one-use
        (one-use ?k - key)
        ; Key ?k is multi-use
        (multi-use ?k - key)
        
    )

    ; IMPORTANT: You should not change/add/remove the action names or parameters

    ;Hero can move if the
    ;    - hero is at current location ?from,
    ;    - hero will move to location ?to,
    ;    - corridor ?cor exists between the ?from and ?to locations
    ;    - there isn't a locked door in corridor ?cor
    ;Effects move the hero, and collapse the corridor if it's "risky" (also causing a mess in the ?to location)
    (:action move

        :parameters (?from ?to - location ?cor - corridor)

        :precondition (and

            (hero-at ?from)
            ;(hero-go-to ?to)
            (corridor-to ?cor ?to)
            (corridor-to ?cor ?from)
            (not(locked ?cor))
            (not(collapsed ?cor))

        )

        :effect (and

            (hero-at ?to)
            (not(hero-at ?from))
            (when (risky ?cor)
                (and
                (collapsed ?cor)
                (messy ?to))
            )

        )
    )

    ;Hero can pick up a key if the
    ;    - hero is at current location ?loc,
    ;    - there is a key ?k at location ?loc,
    ;    - the hero's arm is free,
    ;    - the location is not messy
    ;Effect will have the hero holding the key and their arm no longer being free
    (:action pick-up

        :parameters (?loc - location ?k - key)

        :precondition (and

            (hero-at ?loc)
            (key-here ?k ?loc)
            (free-hand)
            (not(messy ?loc))
        )

        :effect (and

            (not (free-hand))
            (holding ?k)
            (not (key-here ?k ?loc))

        )
    )

    ;Hero can drop a key if the
    ;    - hero is holding a key ?k,
    ;    - the hero is at location ?loc
    ;Effect will be that the hero is no longer holding the key
    (:action drop

        :parameters (?loc - location ?k - key)

        :precondition (and

            (hero-at ?loc)
            (holding ?k)
            (not (free-hand))

        )

        :effect (and

            (not (holding ?k))
            (free-hand)
            (key-here ?k ?loc)
        )
    )


    ;Hero can use a key for a corridor if
    ;    - the hero is holding a key ?k,
    ;    - the key still has some uses left,
    ;    - the corridor ?cor is locked with colour ?col,
    ;    - the key ?k is if the right colour ?col,
    ;    - the hero is at location ?loc
    ;    - the corridor is connected to the location ?loc
    ;Effect will be that the corridor is unlocked and the key usage will be updated if necessary
    (:action unlock

        :parameters (?loc - location ?cor - corridor ?col - colour ?k - key)

        :precondition (and

            (not(free-hand))
            (holding ?k)
            (has-uses ?k)
            (locked-with ?cor ?col)
            (key-colour ?k ?col)
            (hero-at ?loc)
            (corridor-to ?cor ?loc)

        )

        :effect (and

            ; basically decrement key uses left
            (when (one-use ?k)
                (and
                (not (one-use ?k))
                (not (has-uses ?k)))
            )
            (when (two-use ?k)
                (and
                (not (two-use ?k))
                (one-use ?k))
            )
            (not (locked ?cor))
        )
    )

    ;Hero can clean a location if
    ;    - the hero is at location ?loc,
    ;    - the location is messy
    ;Effect will be that the location is no longer messy
    (:action clean

        :parameters (?loc - location)

        :precondition (and

            (hero-at ?loc)
            (messy ?loc)

        )

        :effect (and

            (not (messy ?loc))
        )
    )

)
