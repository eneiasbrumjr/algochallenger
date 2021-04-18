<?php

namespace App\Http\Controllers;

use App\Problem;
use App\Working;
use Illuminate\Foundation\Auth\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Crypt;
use Illuminate\Support\Facades\Storage;
use League\Flysystem\Exception;
use PhpZip\ZipFile;

class ProblemController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index(Request $request, Working $working)
    {
        $user = Auth::user();
        if ($user->isStudent()) {
            if ($working->students->contains($user)) {
                if (!$working->is_multilogin) {
                    if (count($working->students()->wherePivot('user_id', '=', $user->id)->wherePivotNull('ip')->get())) {
                        $working->students()->updateExistingPivot($user, ['ip' => $request->ip()]);
                        $working->save();
                        
                    } else {
                        if (count($working->students()->wherePivot('user_id', '=', $user->id)->wherePivot('ip','=', $request->ip())->get())) {
                            return response()->json($working->problems);
                        }

                        return response()->json(['message' => 'Forbidden'], 403);
                    }
                }
                return response()->json($working->problems);
            }

            return response()->json(['message' => 'Forbidden'], 403);
        }
        return response()->json($working->problems);
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
    public function store(Request $request, Working $working)
    {

        $rules = [
            'name' => 'required',
            'file' => 'file|mimes:zip'
        ];

        $this->validate($request, $rules);

        $zipFile = new ZipFile();

        $uploadedFile = $request->file;
        $problem = new Problem();
        $problem->name = $uploadedFile->getClientOriginalName();
        $problem->full_name = $uploadedFile->getClientOriginalName();

        $problem->base_file_name = $uploadedFile->getClientOriginalName();

        $working->problems()->save($problem);

        $file = Storage::putFileAs("problems/$problem->id", $request->file, $uploadedFile->getClientOriginalName());

        $extractTo = Storage::getDriver()->getAdapter()->getPathPrefix() . "problems/$problem->id";

        $zipFile->openFromString(Storage::get($file))
            ->extractTo($extractTo) // extract files to the specified directory
            ->deleteFromRegex('~^\.~'); // delete all hidden (Unix) files

        $zipFile->close();

        $descriptionFileContents = Storage::get('problems/' . $problem->id . '/description/problem.info');

        $descriptionFileLines = explode("\n", $descriptionFileContents);

        foreach ($descriptionFileLines as $descriptionFileLine) {
            $exploded = explode('=', $descriptionFileLine);
            if ($exploded[0] == 'basename') {
                $problem->name = $exploded[1];
            }
            if ($exploded[0] == 'fullname') {
                $problem->full_name = $exploded[1];
            }
            if ($exploded[0] == 'descfile') {
                $problem->description_file_name = $exploded[1];
            }
        }

        $problem->update();

        return response()->json($problem);
    }

    public function downloadZip(Problem $problem)
    {
        $file = storage_path($problem->zip_path);

        return response()->download($file, $problem->file_name);
    }

    public function downloadDescription(Problem $problem)
    {
        $file = storage_path($problem->description_path);

        return response()->download($file, $problem->file_name);
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Problem  $problem
     * @return \Illuminate\Http\Response
     */
    public function show(Problem $problem)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Problem  $problem
     * @return \Illuminate\Http\Response
     */
    public function edit(Problem $problem)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Problem  $problem
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Problem $problem)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Problem  $problem
     * @return \Illuminate\Http\Response
     */
    public function destroy(Problem $problem)
    {
        //
    }
}
