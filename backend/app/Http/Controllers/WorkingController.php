<?php

namespace App\Http\Controllers;

use App\Working;
use App\User;
use Carbon\Carbon;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class WorkingController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $user = Auth::guard('api')->user();
        if ($user->isAdmin()) {
            return response()->json(Working::orderBy('id', 'asc')->get());
        }
        if ($user->isStudent()) {
            return response()->json($user->workings()->where('start_date', '<', Carbon::now())->get());
        }
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $rules = [
            'name' => 'required',
            'students' => 'array',
            'students.*' => 'exists:users,id'
        ];

        $this->validate($request, $rules);        

        $working = Working::create($request->all());
        $working->students()->sync($request->students, false);
        
        return response()->json($working);
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Working  $working
     * @return \Illuminate\Http\Response
     */
    public function show(Working $working)
    {
        return response()->json($working);
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Working  $working
     * @return \Illuminate\Http\Response
     */
    public function edit(Working $working)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Working  $working
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Working $working)
    {
        $rules = [
            'name' => 'required',
            'students' => 'array',
            'students.*' => 'exists:users,id'
        ];

        $this->validate($request, $rules);        

        $working->update($request->all());
        $working->students()->sync($request->students, false);
        
        return response()->json($working);
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Working  $working
     * @return \Illuminate\Http\Response
     */
    public function destroy(Working $working)
    {
        //
    }

    public function addStudent(Working $working, User $student)
    {
        $working->students()->attach($student);

        return response()->json(['message' => 'Success'], 200);
    }

    public function removeStudent(Working $working, User $student)
    {
        $working->students()->detach($student);

        return response()->json(['message' => 'Success'], 200);
    }

    public function addStudents(Request $request, Working $working)
    {
        $rules = [
            'students' => 'required|array',
            'students.*' => 'exists:users,id'
        ];

        $this->validate($request, $rules);

        $working->students()->sync($request->students, false);

        return response()->json(['message' => 'Success'], 200);
    }
}
