<?php

namespace App\Http\Controllers;

use App\Problem;
use App\Run;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Storage;

class RunController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index(Problem $problem)
    {
        $user = Auth::guard('api')->user();
        if ($user->isAdmin()) {
            return response()->json($problem->runs);
        }
        if ($user->isStudent()) {
            return response()->json($user->runs()->where('problem_id', $problem->id)->get());
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
    public function store(Request $request, Problem $problem)
    {
        $rules = [
            'file' => 'file'
        ];

        $this->validate($request, $rules);

        $uploadedFile = $request->file;
        $run = new Run();
        $run->file_name = $uploadedFile->getClientOriginalName();
        $run->student_id = Auth::guard('api')->user()->id;

        $problem->runs()->save($run);

        Storage::putFileAs("problems/$problem->id/runs/$run->id", $request->file, $uploadedFile->getClientOriginalName());

        return response()->json($run);
    }

    public function downloadFile(Run $run)
    {
        $file = storage_path($run->file_path);

        return response()->download($file, $run->file_name);
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Run  $run
     * @return \Illuminate\Http\Response
     */
    public function show(Run $run)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Run  $run
     * @return \Illuminate\Http\Response
     */
    public function edit(Run $run)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Run  $run
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Run $run)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Run  $run
     * @return \Illuminate\Http\Response
     */
    public function destroy(Run $run)
    {
        //
    }
}
