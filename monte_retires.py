import market_return_sampler   as ms
import contribution_strategies as cs
import distribution_strategies as ds
import monaco as mc


# TODO: take in the following command line arguments as parameters for the sim
# Maybe supply these through an env file instead?
# - starting balance
# - starting date
# - contribution amount
# - contribution freq
# - contribution increase
# - contribution increase freq
# - distribution start date
# - distribution frequency
# - distribution target
# - min distribution
# - distribution delta function (constant, linear, custom?)
# - low/high return thresholds

# TODO: convert these constants into configurable parameters
num_simulations = 1
seed = 0

def monaco_preprocess():
    pass

def monaco_run():
    pass

def monaco_postprocess():
    pass

def run_monte_carlo_sim():
    # keyed functions for the monaco Sim object
    monaco_funcs = {
        mc.SimFunctions.PREPROCESS:  monaco_preprocess,
        mc.SimFunctions.RUN:         monaco_run,
        mc.SimFunctions.POSTPROCESS: monaco_postprocess,
    }

    # create the monaco Sim object
    sim = mc.Sim(
        name='Monte Retires',
        ndraws=num_simulations,
        fcns=monaco_funcs,
        firstcaseismedian=False,
        samplemethod=mc.SampleMethod.SOBOL_RANDOM,
        seed=seed,
        singlethreaded=False,
        savesimdata=False,
        savecasedata=False,
        verbose=True,
        debug=True
    )

    #for date in range():
    #    pass

    # run the monaco simulation
    sim.runSim()

if __name__ == "__main__":
    sim = run_monte_carlo_sim()