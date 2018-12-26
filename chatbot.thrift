/*结构体类型：*/
struct Err
{
  1:i32 errno,
  2:string errmsg,
}

struct UtterenceResult
{
  1:Err err,
  2:string response_content,
  3:list<double> state_matrix,
  4:list<string> candidate,
}

/*服务类型：*/
service chatbotservice {
    Err createDialogue(1:i32 dialog_id),
	Err endDialogue(1:i32 dialog_id),
	UtterenceResult utterenceFuncall(1:i32 dialog_id,2:string utterence),
}
