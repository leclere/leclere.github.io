#!/usr/bin/env python3

import copy
import json
import re
from pathlib import Path


OUTDIR = Path("/home/vincent.leclere@enpc.fr/Documents/Enseignement/TPsol")
CORR = OUTDIR / "IPM_corr.ipynb"
STUDENT = OUTDIR / "IPM_student.ipynb"


def _source(cell):
    return "".join(cell.get("source", []))


def _lines(text: str):
    text = text.strip("\n")
    if not text:
        return []
    return [line + "\n" for line in text.split("\n")]


def _set_source(cell, text: str):
    cell["source"] = _lines(text)
    if cell.get("cell_type") == "code":
        cell["execution_count"] = None
        cell["outputs"] = []


def _replace_answer_blocks(nb):
    for cell in nb["cells"]:
        src = _source(cell)
        if cell.get("cell_type") == "markdown" and 'class="alert alert-info"' in src:
            match = re.search(r"<b>Question ([0-9]+)\)</b>", src)
            if match:
                qnum = match.group(1)
                _set_source(
                    cell,
                    f"""<div class="alert alert-info" role="alert"><b>Question {qnum})</b>
Answer
</div>""",
                )


def _replace_once(text: str, old: str, new: str, label: str):
    if old not in text:
        raise RuntimeError(f"Could not find replacement target for {label}")
    return text.replace(old, new, 1)


def _replace_function(text: str, name: str, replacement: str):
    pattern = re.compile(rf"function {name}\(.*?^end\n?", re.M | re.S)
    new_text, count = pattern.subn(replacement.strip("\n") + "\n", text, count=1)
    if count != 1:
        raise RuntimeError(f"Expected exactly one function named {name}, found {count}")
    return new_text


def _make_barrier_objective_todo(nb):
    old = "barrier_objective(x, s) = s * dot(c, x) + phi(x)"
    new = """function barrier_objective(x, s)
    ### TO COMPLETE:
    ### Return the barrier objective F_s(x) = s*c'x + phi(x).
    error("Complete barrier_objective")
end"""
    for cell in nb["cells"]:
        src = _source(cell)
        if old in src:
            _set_source(cell, _replace_once(src, old, new, "barrier_objective"))
            return
    raise RuntimeError("Could not find barrier_objective")


def _make_newton_step_todo(nb):
    replacement = """
function newton_step(x, s)
    ### TO COMPLETE:
    ### 1. compute the barrier gradient and Hessian,
    ### 2. solve the Newton linear system for dir,
    ### 3. call backtracking_step,
    ### 4. return dir, alpha, and the number of backtracking reductions.
    error("Complete newton_step")
end
"""
    for cell in nb["cells"]:
        src = _source(cell)
        if "function newton_step" in src:
            _set_source(cell, _replace_function(src, "newton_step", replacement))
            return
    raise RuntimeError("Could not find newton_step")


def _make_path_following_todo(nb):
    replacement = """
function path_following_ipm(x0, s0, rho; N_outer = 8, N_inner = 3)
    x = copy(x0)
    s = s0
    all_points = [copy(x)]
    outer_points = [copy(x)]
    steps = Float64[]

    for _ in 1:N_outer
        for _ in 1:N_inner
            ### TO COMPLETE:
            ### Compute one Newton step, update x, and store alpha and x.
            error("Complete the inner loop of path_following_ipm")
        end

        push!(outer_points, copy(x))

        ### TO COMPLETE:
        ### Update the barrier parameter for the next outer iteration.
        error("Complete the outer update of path_following_ipm")
    end

    return (all_points = all_points, outer_points = outer_points, steps = steps, x = x)
end
"""
    for cell in nb["cells"]:
        src = _source(cell)
        if "function path_following_ipm" in src:
            _set_source(cell, replacement)
            return
    raise RuntimeError("Could not find path_following_ipm")


def _make_highs_todo(nb):
    replacement = """
function solve_lp_with_highs(pb)
    n = length(pb.c)
    model = Model(HiGHS.Optimizer)
    set_silent(model)

    ### TO COMPLETE:
    ### Build the JuMP model for min pb.c'x subject to pb.A*x <= pb.b.
    ### Solve it with HiGHS, check that the status is optimal, and return
    ### (x = value.(x), value = objective_value(model), status = status).
    error("Complete solve_lp_with_highs")
end
"""
    for cell in nb["cells"]:
        src = _source(cell)
        if "function solve_lp_with_highs" in src:
            _set_source(cell, replacement)
            return
    raise RuntimeError("Could not find solve_lp_with_highs")


def _make_fixed_inner_todo(nb):
    replacement = """
function fixed_inner_pb_until_gap(pb, x_centered, s0, rho, N_inner, opt_value;
        eps = 5e-3, max_outer = 80, max_s = 1e8)
    x = copy(x_centered)
    s = s0
    linear_solves = 0
    total_backtracks = 0
    min_alpha = 1.0
    best_gap = max(dot(pb.c, x) - opt_value, 0.0)

    for outer in 1:max_outer
        ### TO COMPLETE:
        ### 1. update s using rho,
        ### 2. perform N_inner Newton steps,
        ### 3. count linear solves and backtracking reductions separately,
        ### 4. update the best optimality gap,
        ### 5. return as soon as best_gap <= eps.
        error("Complete fixed_inner_pb_until_gap")
    end

    return (
        rho = rho,
        N_inner = N_inner,
        solved = false,
        outer_updates = max_outer,
        linear_solves = linear_solves,
        final_gap = best_gap,
        final_s = s,
        total_backtracks = total_backtracks,
        min_alpha = min_alpha,
    )
end
"""
    for cell in nb["cells"]:
        src = _source(cell)
        if "function fixed_inner_pb_until_gap" in src:
            _set_source(cell, replacement)
            return
    raise RuntimeError("Could not find fixed_inner_pb_until_gap")


def _add_student_marker(nb):
    for cell in nb["cells"]:
        src = _source(cell)
        if src.startswith("# Interior point methods for linear programming"):
            src = src.replace(
                "# Interior point methods for linear programming",
                "# Interior point methods for linear programming -- student version",
                1,
            )
            _set_source(cell, src)
            return


def build_student(corr_nb):
    student = copy.deepcopy(corr_nb)
    _add_student_marker(student)
    _replace_answer_blocks(student)
    _make_barrier_objective_todo(student)
    _make_newton_step_todo(student)
    _make_path_following_todo(student)
    _make_highs_todo(student)
    _make_fixed_inner_todo(student)
    return student


def main():
    corr_nb = json.loads(CORR.read_text(encoding="utf-8"))
    student_nb = build_student(corr_nb)
    STUDENT.write_text(json.dumps(student_nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {STUDENT}")


if __name__ == "__main__":
    main()
