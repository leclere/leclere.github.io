using Random
using IterTools

faces = ("brain","steps","shotgun")

dices_prob = Dict()
dices_prob["green"] = Dict("brain"=> 3/6, "steps"=> 2/6 ,"shotgun"=> 1/6 )
dices_prob["orange"] = Dict("brain"=> 2/6, "steps"=> 2/6 ,"shotgun"=> 2/6 )
dices_prob["red"] = Dict("brain"=> 1/6, "steps"=> 2/6 ,"shotgun"=> 3/6 )


########################################################################
#    Helper functions
########################################################################
# initialise the state
function init_state()
    initial_bag = Dict("green"=>6,"orange"=>4,"red"=>3)
    initial_steps = Dict("green"=>0,"orange"=>0,"red"=>0)
    return Dict("brains_acc"=>0, "shotguns_acc"=>0,"bag"=>initial_bag,"steps"=>initial_steps)
end

#compute the number of dices still in the bag
function sum_bag(state)
    nb_in_bag = state["bag"]
    nb = nb_in_bag["green"] + nb_in_bag["orange"] + nb_in_bag["red"]
    nb < 0 && error("negative number of dice in the bag")
    return nb
end

#compute the number of dices in step
function sum_steps(state)
    nb_steps = state["steps"]
    nb = nb_steps["green"] + nb_steps["orange"] + nb_steps["red"] 
    nb > 3 && error("more than 3 dices in steps")
    return nb
end

function eval_position!(state;verbose =0)
    #evaluate position at the end of a throw
    have_to_stop = false
    if state["shotguns_acc"] > 2 #stunned by shotgun
        verbose > 0 && println("stunned by $(state["shotguns_acc"]) shotgun wounds")
        return (0, true)
    elseif sum_bag(state) + sum_steps(state) <3 # not enough dices
        verbose > 0 && println("ran out of dice, earned $(state["brains_acc"]) brains")
        return ( state["brains_acc"], true)
    end
    return ( state["brains_acc"], false)
end

function sum_up(state)
    println("$(state["brains_acc"]) brains, $(state["shotguns_acc"]) shotgun, $(state["steps"]["green"]) green step, $(state["steps"]["orange"]) orange step, $(state["steps"]["red"]) red step, $(sum_bag(state)) dices in bag")
end

########################################################################
#    Inner simulation functions
########################################################################

# Select randomly one dice in the bag 
function select_1_dice!(state;verbose =0)
    rnd = rand(1:sum_bag(state))
    nb_in_bag=state["bag"]
    if rnd <= nb_in_bag["green"]
        color = "green"
    elseif rnd <= nb_in_bag["green"] + nb_in_bag["orange"]
        color = "orange"
    else 
        color = "red"
    end
    verbose > 1 && println("Draw a $color dice from the bag")
    state["bag"][color] -= 1
    return color
end

# roll a dice of given color
function roll_dice!(color,state;verbose =0)
    rnd = rand()
    if rnd <= dices_prob[color]["brain"] #rolled a brain
        state["brains_acc"] += 1
        verbose > 2 && println("rolled a brain from a $color dice") 
    elseif rnd <= dices_prob[color]["brain"] + dices_prob[color]["steps"] #rolled steps
        state["steps"][color] += 1
        verbose > 2 && println("rolled steps from a $color dice") 
    else 
        state["shotguns_acc"] += 1 #rolled shotgun
        verbose > 2 && println("rolled shotgun from a $color dice")
    end
end

########################################################################
#    Simulator functions
########################################################################

#Update state once the player has decided to make a throw
function make_a_throw!(state;verbose =0)
    nb_steps = sum_steps(state)
    nb_steps > 3 && error("more than 3 step")
    
    # rolling the current dices hold
    current_steps = state["steps"]
    state["steps"] = Dict("green"=>0,"orange"=>0,"red"=>0)
    
    for (color,nb) in current_steps
        for _ in 1:nb
            verbose > 1 && println("rolling a stepped $color dice")
            roll_dice!(color,state,verbose = verbose)
        end
    end
    
    #drawing and rolling new dices
    for _ in 1:3-nb_steps
        color = select_1_dice!(state,verbose = verbose)
        verbose > 1 && println("rolling a new $color dice")
        roll_dice!(color,state,verbose=verbose)
    end
end

#Simulate a turn, making throw until player decide to stop
#return number of brains obtained
function make_a_turn!(policy;verbose =0)
    state = init_state()

    throw_again = true
    while throw_again
        make_a_throw!(state,verbose = verbose)
        res, forced_stop = eval_position!(state,verbose = verbose)
        verbose > 4 && println(state)
        forced_stop && return res 
        throw_again = policy(state)
        verbose >0 && sum_up(state)
    end
    return(state["brains_acc"])
end


# simulate Nmc turn, return average number of brains earned
function simulate(policy;Nmc = 1000, verbose=0)
    res = 0
    for _ in 1:Nmc
        res += make_a_turn!(policy;verbose =verbose)
    end
    return res / Nmc
end

########################################################################
#    Test functions
########################################################################

## A policy take as argument a state and return a boolean true if you continue, false otherwise
function all_in_policy(state)
    return true
end

simulate(all_in_policy;Nmc=1e4,verbose = 0)
